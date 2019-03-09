import QtQuick 2.5
import QtQuick.Window 2.2
import QtQuick.Layouts 1.3
import QtQuick.Controls 1.4
import io.thp.pyotherside 1.4

Window {
    id: window
    width: 360
    height: 360
    title: "Gravatar"
    
    ColumnLayout {
        spacing: 2
        anchors.fill: parent
    
        Image {
            id: avatar
            source: ""
            fillMode: Image.PreserveAspectFit
            Layout.fillHeight: true
            Layout.fillWidth: true
        }
        Label {
            id: error_label
            Layout.fillWidth: true
        }
        TextField {
            id: mailinput
            width: parent.width
            text: "mail@example.com"
            Layout.fillWidth: true
            onEditingFinished:
            {
                py.call("gravatar.get", [mailinput.text], function(result) {
                    if(result["status"] == "ok") {
                        avatar.source = result["url"];
                        error_label.text = "";
                    } else {
                        avatar.source = "";
                        error_label.text = result["error"];
                    }
                });
            }
        }
    }
    Python {
        id: py
        Component.onCompleted:
        {
            // Add the directory of this .qml file to the search path
            addImportPath(Qt.resolvedUrl('.'));
            // Import the main module and load the data
            importModule('gravatar', null);
        }
        onError:
        {
            error_label.text = traceback;
        }
    }
}
