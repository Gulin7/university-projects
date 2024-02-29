package Controller;


import ADT.statement.IStmt;
import ADT.PrgState;
import ADT.stack.MyIStack;
import ADT.value.RefValue;
import ADT.value.Value;
import repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller {
    IRepository repo;
    boolean flag;

    public Controller(IRepository repo){
        this.repo= repo;
    }
    public PrgState oneStep(PrgState state) throws MyException {
        MyIStack<IStmt> stk=state.getExeStack();
        if(stk.isEmpty()) {
            throw new MyException("prgstate stack is empty");
        }
        IStmt crtStmt = stk.pop();
        return crtStmt.execute(state);
    }

    public void setFlag(boolean flag){
        this.flag = flag;
    }

    public void allStep() throws MyException {
        PrgState prg = repo.getCrtPrg(); // repo is the controller field of type MyRepoInterface
        repo.logPrgStateExec();
        while (!prg.getExeStack().isEmpty()){
            oneStep(prg);
            repo.logPrgStateExec();
            prg.getHeap().setContent(safeGarbageCollector(
                    getAddressesFromSymTableOrHeap(prg.getSymTable().getMap().values()),
                    getAddressesFromSymTableOrHeap(prg.getHeap().getContent().values()),
                    prg.getHeap().getContent()
            ));
            if(flag == true)
            {
                System.out.println(prg);
            }
        }
        if(flag == false){
            System.out.println(prg);
        }
    }

    public Map<Integer, Value> safeGarbageCollector(List<Integer> symTableAddresses, List<Integer> heapAddresses, Map<Integer, Value> heap) {
        return heap.entrySet().stream()
                .filter(e -> ( symTableAddresses.contains(e.getKey()) || heapAddresses.contains(e.getKey())))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }

    public List<Integer> getAddressesFromSymTableOrHeap(Collection<Value> symTableValuesOrHeap) {
        return symTableValuesOrHeap.stream()
                .filter(v -> v instanceof RefValue)
                .map(v -> {RefValue v1 = (RefValue) v; return v1.getAddr();})
                .collect(Collectors.toList());
    }

}
