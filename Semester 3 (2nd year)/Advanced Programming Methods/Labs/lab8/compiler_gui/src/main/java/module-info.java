module ubb.compiler_gui {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;

    opens source to javafx.fxml;
    //exports ubb;
    exports source.controller;
    opens source.controller to javafx.fxml;
    exports source.ui.gui;
    opens source.ui.gui to javafx.fxml;
    exports source.controller.gui_controllers;
    opens source.controller.gui_controllers to javafx.fxml;
}