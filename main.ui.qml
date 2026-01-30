import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 640
    height: 480
    color: '#450606'

    Text {
        anchors.centerIn: parent
        text: qsTr("Hello World")
        font.pixelSize: 24
        color: '#e26565'
    }
}
    