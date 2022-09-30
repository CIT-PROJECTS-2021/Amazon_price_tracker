#####Amazon_price_tracker

***A python project to track price changes on Amazon.

***This is how Amazon_price_tracker was setup




***The functionality of the Amazon_price_tracker

Alert you as soon as it detects a price drop 

Should allow you to track any product on Amazon, not restricting you to a certain selection of products

Include a free chrome browser extension to easily create price drop alerts 

from PyQt6.QtWidgets: import (QApplication, QLabel, QMainWindow, QPushButton,
                             QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QTableWidget, QTableWidgetItem
                             )
import sys

dummy_data = {
    "Iphone": [10000, 20000, 30000, 40000],
    "Television": [70000, 80000, 90000, 100000],
    "Comb": [40, 30, 70, 10, 50, 40, 30, 30, 30,
             30,  20, 40, 30, 70, 10, 50, 40, 30,
             30, 30, 30,  20, 40, 30],
    "Socks": [10000, 20000, 30000, ],
    "Bicycles": [40, 30, 70, 10, 50, 40, 30, 30, 30,
                 30,  20, ]
}


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle('Youtube Transcripts Converter')
        self.setGeometry(200, 100, 1000, 600)
        center_widget = QWidget(self)
        center_widget_layout = QVBoxLayout()
        center_widget_layout.addWidget(self._create_search_input())
        center_widget_layout.addWidget(self._create_tracking_table())
        center_widget.setLayout(center_widget_layout)
        self.setCentralWidget(center_widget)

    def _create_search_input(self):
        search_widget = QWidget()
        search_widget.setFixedHeight(50)
        search_widget.setFixedWidth(500)
        layout = QHBoxLayout()

        # Input Label
        layout.addWidget(QLabel("Enter Item Here: "))

        # Form Input
        form_input = QLineEdit()
        form_input.setFixedWidth(300)
        layout.addWidget(form_input)

        # button
        button = QPushButton("Track")
        layout.addWidget(button)

        search_widget.setLayout(layout)

        def add_to_tracking():
            item = form_input.text()
            return item

        button.clicked.connect(lambda: add_to_tracking())

        return search_widget

    def _create_tracking_table(self):
        horizontal_label = ["Item"]

        table = QTableWidget()
        row_count = len(dummy_data.keys())
        table.setRowCount(row_count)
        table.setColumnCount(25)
        for i in range(1, 25):
            if i == 1:
                hour_label = str(i) + "Hr"
                horizontal_label.append(hour_label)
            else:
                hour_label = str(i) + "Hrs"
                horizontal_label.append(hour_label)

        table.setHorizontalHeaderLabels(horizontal_label)

        v_label = list(dummy_data.keys())

        for i in v_label:
            item_name = QTableWidgetItem(i)
            table.setItem(v_label.index(i), 0, item_name)

        prices = list(dummy_data.values())

        for i in prices:
            for index, cost in enumerate(i):
                item_price = QTableWidgetItem(str(cost))
                table.setItem(prices.index(i), index+1, item_price)

        return table


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


***How the Amazon_price_tracker notifications 

When the Amazon price tracker detects a price change, it sends the user a notification, 
alerting them of the price drop. An Amazon price tracker also monitors prices to several websites at once,
so you can compare price drops between different retailers and unveil the lowest price.

![image](https://user-images.githubusercontent.com/111295447/193137014-f8df307c-ea74-41d1-83d7-e2e8f101ec92.png)



