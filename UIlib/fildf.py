import ipywidgets as widgets
from IPython.display import display, clear_output
import pandas as pd
from ipywidgets import interactive_output

class DataFrameOperations:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.column_selector = widgets.Dropdown(
            options=[''] + list(dataframe.columns),
            description='Select Column:'
        )
        self.unique_values_selector = widgets.SelectMultiple(
            options=[],
            description='Select Unique Values:'
        )
        self.parameter_input = widgets.Text(
            description='Enter parameter (substring/regex):'
        )
        self.operation_selector = widgets.Dropdown(
            options=['sunique', 'svalue_counts', 'scontains', 'smatch', 'sgroupby', 'sdataws'],
            description='Select Operation:'
        )
        self.output = widgets.Output()
        self.container = widgets.VBox([
            self.column_selector, 
            self.unique_values_selector, 
            self.parameter_input, 
            self.operation_selector, 
            self.output
        ])
        self.setup_widget()
        display(self.container)

    def setup_widget(self):
        self.unique_values_selector.layout.width = '700px'             
        self.column_selector.observe(self.update_unique_values, names='value')
        interactive_output(self.perform_operation, 
                           {'column': self.column_selector, 
                            'unique_values': self.unique_values_selector, 
                            'parameter': self.parameter_input, 
                            'operation': self.operation_selector})

    def update_unique_values(self, change):
       selected_column = self.column_selector.value
       if selected_column:
         unique_values = list(self.dataframe[selected_column].unique())
       else:
          unique_values = []
       self.unique_values_selector.options = unique_values
       self.unique_values_selector.value = () 

    def perform_operation(self, column, unique_values, parameter, operation):
        # Implement your logic based on selected column, unique values, parameter, and operation
        # Clear the output before displaying new content
        with self.output:
            clear_output(wait=True)
            print("Performing operation:", operation)
            print("Selected Column:", column)
            print("Selected Values:", unique_values)
            print("Parameter:", parameter)
            try:
             if operation == 'sunique':
                result = self.sunique(column)
             elif operation == 'svalue_counts':
                result = self.svalue_counts(column)
             elif operation == 'scontains':
                result = self.scontains(column, parameter)
             elif operation == 'smatch':
                result = self.smatch(column, parameter)
             elif operation == 'sgroupby':
                result = self.sgroupby(parameter)
             elif operation == 'sdataws':
                result = self.sdataws(column, unique_values)

             display(result)
            except Exception as e:
               print("Error:", e)

    def sunique(self, column):
        return self.dataframe[column].unique()

    def svalue_counts(self, column):
        return self.dataframe[column].value_counts()

    def scontains(self, column, substring):
        return self.dataframe[self.dataframe[column].str.contains(substring, na=False)]

    def smatch(self, column, regex):
        return self.dataframe[self.dataframe[column].str.match(regex, na=False)]

    def sgroupby(self, column):
        parameter=parameter.split(',')
        df = self.dataframe.copy()
        return df.groupby(df[parameter[0]])[parameter[1:]].value_counts().reset_index()

    def sdataws(self, column, selected_values):
        print("Selected Column:", column)
        print("Selected Values:", selected_values)
        # Filter DataFrame where the selected column contains any of the selected unique values
        return self.dataframe[self.dataframe[column].isin(selected_values)]
            # Implement your operation logic and display the result here
            

#pass your dataframe here
widget_instance = DataFrameOperations(dataframe)
