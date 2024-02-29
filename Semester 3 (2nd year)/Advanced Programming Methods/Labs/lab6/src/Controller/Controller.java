package Controller;


import ADT.PrgState;
import ADT.value.RefValue;
import ADT.value.Value;
import repository.IRepository;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    IRepository repo;
    boolean flag;
    ExecutorService executor;

    public Controller(IRepository repo) {
        this.repo = repo;
    }

    //    public PrgState oneStep(PrgState state) throws MyException {
//        MyIStack<IStmt> stk=state.getExeStack();
//        if(stk.isEmpty()) {
//            throw new MyException("prgstate stack is empty");
//        }
//        IStmt crtStmt = stk.pop();
//        return crtStmt.execute(state);
//    }
    public IRepository getRepo() {
        return this.repo;
    }

    List<PrgState> removeCompletedPrg(List<PrgState> inPrgList) {
        return inPrgList.stream().filter(p -> p.isNotCompleted()).collect(Collectors.toList());
    }

    public void setFlag(boolean flag) {
        this.flag = flag;
    }


    public void oneStepForAllPrg(List<PrgState> prgList) throws MyException, InterruptedException {
        prgList.forEach(prg -> {
            try {
                repo.logPrgStateExec(prg);
            } catch (MyException e) {
                System.out.println(e.getMessage());
            }
        });
        List<Callable<PrgState>> callList = prgList.stream()
                .map((PrgState p) -> (Callable<PrgState>) (() -> {
                    return p.oneStep();
                })).collect(Collectors.toList());

        List<PrgState> newPrgList = executor.invokeAll(callList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (InterruptedException e) {
                        System.out.println(e.getMessage());
                        System.exit(1);
                    } catch (ExecutionException e) {
                        System.out.println(e.getMessage());
                        System.exit(1);
                    }
                    return null;
                }).filter(p -> p != null).collect(Collectors.toList());
        prgList.addAll(newPrgList);
        prgList.forEach(prg -> {
            try {
                fullSafeGarbageCollector(prgList);
                repo.logPrgStateExec(prg);
            } catch (MyException e) {
                System.out.println(e.getMessage());
            }
        });
        repo.setPrgList(prgList);

//        while (!prg.getExeStack().isEmpty()){
//            oneStep(prg);
//            repo.logPrgStateExec();
//            prg.getHeap().setContent(safeGarbageCollector(
//                    getAddressesFromSymTableOrHeap(prg.getSymTable().getMap().values()),
//                    getAddressesFromSymTableOrHeap(prg.getHeap().getContent().values()),
//                    prg.getHeap().getContent()
//            ));
//            if(flag)
//            {
//                System.out.println(prg);
//            }
//        }
//        if(!flag){
//            System.out.println(prg);
//        }
    }

    public void allStep() throws MyException, InterruptedException {
        executor = Executors.newFixedThreadPool(2);
        //remove the completed programs
        List<PrgState> prgList = removeCompletedPrg(repo.getPrgList());
        while (!prgList.isEmpty()) {
            fullSafeGarbageCollector(prgList);
            //HERE you can call conservativeGarbageCollector
            oneStepForAllPrg(prgList);
            //remove the completed programs
            prgList = removeCompletedPrg(repo.getPrgList());
        }
        executor.shutdownNow();
        prgList = removeCompletedPrg(repo.getPrgList());
        repo.setPrgList(prgList);
    }

    public void fullSafeGarbageCollector(List<PrgState> prgList) {
        prgList.forEach(
                p -> {
                    p.getHeap().setContent(safeGarbageCollector(getAddressesFromSymTableOrHeap(p.getSymTable().getMap().values()), getAddressesFromSymTableOrHeap(p.getHeap().getContent().values()), p.getHeap().getContent()));
                }
        );
    }

    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddresses, List<Integer> heapAddresses, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> (symTableAddresses.contains(e.getKey()) || heapAddresses.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public List<Integer> getAddressesFromSymTableOrHeap(Collection<Value> symTableValuesOrHeap) {
        return symTableValuesOrHeap.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {
                    RefValue v1 = (RefValue) v;
                    return v1.getAddr();
                })
                .collect(Collectors.toList());
    }

}
