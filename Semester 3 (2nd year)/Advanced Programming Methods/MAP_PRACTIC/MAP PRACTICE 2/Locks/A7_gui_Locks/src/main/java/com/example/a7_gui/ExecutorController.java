package com.example.a7_gui;

import com.example.a7_gui.controller.Controller;
import com.example.a7_gui.exceptions.InterpreterException;
import com.example.a7_gui.model.programState.ProgramState;
import com.example.a7_gui.model.stmt.IStatement;
import com.example.a7_gui.model.utils.MyIDictionary;
import com.example.a7_gui.model.utils.MyIHeap;
import com.example.a7_gui.model.utils.MyILockTable;
import com.example.a7_gui.model.utils.MyISymbolTable;
import com.example.a7_gui.model.values.Value;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

class AditionalStructure<T,S>{
    T first;
    S second;

    public AditionalStructure(T f, S s)
    {
        this.first=f;
        this.second=s;
    }
}

public class ExecutorController {
    public Button runOneStepButton;
    private Controller controller;

    @FXML
    private TextField numberOfProgramStatesField;
    @FXML
    private ListView<String> outputListView;
    @FXML
    private ListView<String> fileTableListView;
    @FXML
    private ListView<Integer> programIdsListView;
    @FXML
    private ListView<String> executionStackListView;
    @FXML
    private TableView<AditionalStructure<String,Value>> symbolTableView;
    @FXML
    private TableColumn<AditionalStructure<String,Value>,String> variableName;
    @FXML
    private TableColumn<AditionalStructure<String,Value>,String> variableValue;
    @FXML
    private TableView<AditionalStructure<Integer, Value>> heapTableView;
    @FXML
    private TableColumn<AditionalStructure<Integer,Value>, Integer> heapAddress;
    @FXML
    private TableColumn<AditionalStructure<Integer,Value>, String> heapValue;
    @FXML
    private TableView<AditionalStructure<Integer,Integer>> lockTableView;
    @FXML
    private TableColumn<AditionalStructure<Integer, Integer>, String> lockAddress;
    @FXML
    private TableColumn<AditionalStructure<Integer, Integer>, String> lockValue;
    public void setController(Controller ctrl)
    {
        this.controller=ctrl;
        populateAllItems();
    }

    @FXML
    public void initialize()
    {
        programIdsListView.getSelectionModel().setSelectionMode(SelectionMode.SINGLE);
        heapAddress.setCellValueFactory(p -> new SimpleIntegerProperty(p.getValue().first).asObject());
        heapValue.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));

        variableName.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().first));
        variableValue.setCellValueFactory(p -> new SimpleStringProperty(p.getValue().second.toString()));

        lockAddress.setCellValueFactory(p -> new SimpleObjectProperty<>(p.getValue().first.toString()));
        lockValue.setCellValueFactory(p -> new SimpleObjectProperty<>(p.getValue().second.toString()));
    }

    private ProgramState getCurrentProgramState()
    {
        if(controller.getProgramStates().size() == 0)
            return null;
        else{
            int currentId = programIdsListView.getSelectionModel().getSelectedIndex();
            if(currentId == -1)
                return controller.getProgramStates().get(0);
            else return controller.getProgramStates().get(currentId);
        }
    }

    private void populateAllItems()
    {
        populateProgramIdentifiersListView();
        populateExecutionStackListView();
        populateSymbolTableView();
        populateHeapTableView();
        populateFileTableListView();
        populateOutputListView();
        populateNewTableView();
    }

    private void populateNewTableView() {
        ProgramState programState = getCurrentProgramState();

        MyILockTable lockTable = Objects.requireNonNull(programState).getLockTable();
        ArrayList<AditionalStructure<Integer, Integer>> lockTableEntries = new ArrayList<>();

        for(Map.Entry<Integer, Integer> entry: lockTable.getContent().entrySet()) {
            lockTableEntries.add(new AditionalStructure<>(entry.getKey(), entry.getValue()));
        }

        lockTableView.setItems(FXCollections.observableArrayList(lockTableEntries));
    }

    @FXML
    private void switchProgramState(MouseEvent mouseEvent)
    {
        populateExecutionStackListView();
        populateSymbolTableView();
    }

    private void populateNumberOfProgramStatesField()
    {
        List<ProgramState> programStates = controller.getProgramStates();
        numberOfProgramStatesField.setText(String.valueOf(programStates.size()));
    }

    private void populateHeapTableView()
    {
        ProgramState programState = getCurrentProgramState();
        MyIHeap heap = Objects.requireNonNull(programState).getHeap();
        ArrayList<AditionalStructure<Integer,Value>> heapEntries = new ArrayList<>();

        for(Map.Entry<Integer,Value> entry : heap.getContent().entrySet())
            heapEntries.add(new AditionalStructure<>(entry.getKey(), entry.getValue()));

        heapTableView.setItems(FXCollections.observableArrayList(heapEntries));
    }

    private void populateOutputListView()
    {
        ProgramState programState = getCurrentProgramState();
        List<String> output = new ArrayList<>();
        List<Value> outputList = Objects.requireNonNull(programState).getOut().getList();

        for (Value value : outputList) output.add(value.toString());

        outputListView.setItems(FXCollections.observableArrayList(output));
    }

    private void populateFileTableListView()
    {
        ProgramState programState = getCurrentProgramState();
        List<String> fileNames = new ArrayList<>(Objects.requireNonNull(programState).getFileTable().getContent().keySet());
        fileTableListView.setItems(FXCollections.observableArrayList(fileNames));
    }

    private void populateProgramIdentifiersListView()
    {
        List<ProgramState> programStates = controller.getProgramStates();
        List<Integer> idList = programStates.stream()
                .map(ProgramState::getId)
                .collect(Collectors.toList());
        programIdsListView.setItems(FXCollections.observableList(idList));
        populateNumberOfProgramStatesField();
    }

    private void populateSymbolTableView()
    {
        ProgramState programState = getCurrentProgramState();
        MyISymbolTable<String,Value> symbolTable = Objects.requireNonNull(programState).getSymTable();
        ArrayList<AditionalStructure<String,Value>> symbolTableEntries = new ArrayList<>();

        for(Map.Entry<String,Value> entry : symbolTable.getContent().entrySet())
            symbolTableEntries.add(new AditionalStructure<>(entry.getKey(),entry.getValue()));

        symbolTableView.setItems(FXCollections.observableArrayList(symbolTableEntries));
    }

    private void populateExecutionStackListView()
    {
        ProgramState programState = getCurrentProgramState();
        List<String> executionStackString = new ArrayList<>();

        if(programState != null)
            for (IStatement stmt : programState.getExeStack().getReversed())
                executionStackString.add(stmt.toString());

        executionStackListView.setItems(FXCollections.observableArrayList(executionStackString));
    }

    @FXML
    private void oneStep(MouseEvent event)
    {
        if(controller != null)
        {
            try{
                List<ProgramState> programStates = Objects.requireNonNull(controller.getProgramStates());

                if(programStates.size() > 0)
                {
                    controller.oneStep();
                    populateAllItems();
                    programStates = controller.removeCompletedPrg(controller.getProgramStates());
                    controller.setProgramStates(programStates);
                    populateProgramIdentifiersListView();
                }
                else {
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setTitle("error");
                    alert.setContentText("Nothing left to execute");
                    alert.showAndWait();
                }
            }catch(InterruptedException | InterpreterException e)
            {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setContentText(e.getMessage());
                alert.showAndWait();
            }
        }
        else {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setContentText("No program was selected");
            alert.showAndWait();
        }
    }
}
