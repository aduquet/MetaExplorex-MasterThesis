from django.shortcuts import redirect, render
from django.urls import reverse
import pandas as pd
from django.contrib import messages
from django.http import JsonResponse
from django.http import FileResponse

def home(request):
    if request.method == 'POST':
        num_mrs = request.POST.get('num_mrs')
        print("MRsHome: ", num_mrs)
        file_type = request.POST.get('file_type')
        return redirect(reverse('metalogs') + f'?num_mrs={num_mrs}&file_type={file_type}')

    return render(request, 'metalogs/home.html')

def metalogs(request):
    num_mrs = request.GET.get('num_mrs')
    file_type = request.GET.get('file_type')
    print("MRs: ", num_mrs)
    if request.method == 'GET':
        return render(request, 'metalogs/metalogs.html', get_initial_context())

    result = process_uploaded_file(request, num_mrs, file_type)
    
    if isinstance(result, dict):
        return render(request, 'metalogs/charts.html', result)
    elif result == 'upload':
        return render(request, 'metalogs/metalogs.html')
    else:
        return process_uploaded_file(request, num_mrs, file_type)




def process_uploaded_file(request, num_mrs, file_type):
    if num_mrs is None:
            messages.error(request, 'Number of MRs is missing.')
            return 'upload'    
    uploaded_file = request.FILES.get('file')
    if not uploaded_file:
        messages.error(request, 'No file uploaded')
        return 'upload'
    
    try:
        log_csv = pd.read_csv(uploaded_file)
        is_multiple_type = file_type == 'multiple'
        missing_columns = get_missing_columns(log_csv, is_multiple_type, int(num_mrs))

        if missing_columns:
            messages.error(request, f'Missing columns in log file: {", ".join(missing_columns)}')
            return 'upload'
        
        chart_data = get_chart_data(log_csv)
        chart_data2 = get_chart_data2(log_csv)
        chart_data3 = get_chart_data3(log_csv)
        chart_data4 = get_chart_data4(log_csv)
        chart_data5 = get_chart_data5(log_csv)
        chart_data6 = get_chart_data5(log_csv)
        chart_data7 = get_chart_data7(log_csv)
        
        return {
            'missing_columns': None,
            'chart_data': chart_data,
            'chart_data2': chart_data2,
            'chart_data3': chart_data3,
            'chart_data4': chart_data4,
            'chart_data5': chart_data5,
            'chart_data6': chart_data6,
            'chart_data7': chart_data7,
        }

    except pd.errors.EmptyDataError as e:
        messages.error(request, 'The uploaded file is empty or in an unsupported format.')
        return 'upload'

    except Exception as e:
        messages.error(request, str(e))
        return 'upload'


def get_initial_context():
    return {
        'missing_columns': None,
        'chart_data': None,
        'chart_data2': None,
        'chart_data3': {'labels': [], 'data': []},
        'chart_data4': None,
        'chart_data5': None,
        'chart_data6': None,
        'chart_data7': None,
    }

def get_missing_columns(log_csv, is_multiple_type, num_mrs):
    all_columns = log_csv.columns
    if  len(all_columns) == 3 * num_mrs + 3:
        if is_multiple_type:
            mr_columns = [
                f"input_testData",
                f"MR_Transformed",
                f"output_testInput",
                f"output_MR",
                f"MR_checker",
            ]
            required_columns = ['output_testInput', 'output_MR', 'MR_checker']
            print("Multiple required columns: ",required_columns)
        else:
            mr_checker_columns = [f"MR{i}_checker" for i in range(1, num_mrs + 1)]
            transformed_test_columns = [f"MR{i}_Transformed" for i in range(1, num_mrs + 1)]
            required_columns = [
                "input_testData",
                *transformed_test_columns,
                "output_testInput",
            ] + [f"output_MR{i}" for i in range(1, num_mrs + 1)] + mr_checker_columns 
    return [col for col in required_columns if col not in log_csv.columns]

def get_chart_data(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    input_test_columns = log_csv.filter(like='input_testData').columns
    output_testInput_columns = log_csv.filter(like='output_testInput').columns
    rule_violations = log_csv[checker_columns].apply(lambda x: (x == 'Violated').sum())

    violated_checker_columns = checker_columns[log_csv[checker_columns].eq('Violated').any()]
    input_testData_with_violations = log_csv[input_test_columns].loc[log_csv[violated_checker_columns].eq('Violated').any(axis=1)].values.tolist() 
    output_testInput = log_csv[output_testInput_columns].loc[log_csv[violated_checker_columns].eq('Violated').any(axis=1)].values.tolist() 
    violated_MRchecker = {col: log_csv[col].tolist() for col in checker_columns}
    

    # print("Rulekskkskdks",output_testInput)
    labels = checker_columns.tolist()
    data = rule_violations.tolist()
    return {
            'labels': labels, 
            'data': data, 
            'input_testData_with_violations': input_testData_with_violations, 
            'violated_MRchecker': violated_MRchecker,
            'output_testInput': output_testInput
            }

def get_chart_data2(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    rule_violations = log_csv[checker_columns].apply(lambda x: (x == 'Not-violated').sum())
    labels = checker_columns.tolist()
    data = rule_violations.tolist()
    return {'labels': labels, 'data': data}

def get_chart_data3(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    crashed_rows = log_csv[checker_columns].apply(lambda x: x[~x.isin(['Violated', 'Not-violated'])].count())
    labels = checker_columns.tolist()
    data = crashed_rows.tolist()
    return {'labels': labels, 'data': data}

def get_chart_data4(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    not_crashed_rows = log_csv[checker_columns].apply(lambda x: x[x.isin(['Violated', 'Not-violated'])].count())
    labels = checker_columns.tolist()
    data = not_crashed_rows.tolist()
    return {'labels': labels, 'data': data}



def get_chart_data5(log_csv):
    chart_data5_list = []
    required_columns = log_csv.filter(like='_checker').columns
    
    for idx, column in enumerate(required_columns):
        rule_name = column.replace("_checker", "")
        violated_rows = log_csv[log_csv[column] == 'Violated']
        output_column = f'output_{rule_name}'
        
        if output_column not in log_csv.columns:
            continue  
        cleaned_values = violated_rows[output_column].apply(pd.to_numeric, errors='coerce').dropna()

        if not cleaned_values.empty:
            chart_data5_list.append({
                'label': f'{output_column} for {rule_name} Violations',
                'data': cleaned_values.tolist(),
                'backgroundColor': 'rgba(255, 125, 77, 0.5)',
                'borderColor': 'rgba(255, 125, 77, 1)',
                'borderWidth': 1,
            })

    labels = [item['label'] for item in chart_data5_list]
    datasets = chart_data5_list
    return {'labels': labels, 'datasets': datasets}

def get_chart_data6(log_csv):
    chart_data_list = []
    required_columns = log_csv.filter(like='_checker').columns
    
    for idx, column in enumerate(required_columns):
        rule_name = column.replace("_checker", "")
        non_violated_rows = log_csv[log_csv[column] == 'Not-violated']  
        output_column = f'output_{rule_name}'
        if output_column not in log_csv.columns:
            continue  
        cleaned_values = non_violated_rows[output_column].apply(pd.to_numeric, errors='coerce').dropna()
        if not cleaned_values.empty:
            chart_data_list.append({
                'label': f'{output_column} for {rule_name} Non-Violations',  
                'data': cleaned_values.tolist(),
                'backgroundColor': 'rgba(77, 125, 255, 0.5)',  
                'borderColor': 'rgba(77, 232, 255, 1)',
                'borderWidth': 1,
            })

    labels = [item['label'] for item in chart_data_list]
    datasets = chart_data_list
    return {'labels': labels, 'datasets': datasets}


def get_chart_data7(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    num_mrs = len(checker_columns)
    rule_violations = log_csv[checker_columns].apply(lambda x: (x == 'Violated').sum())
    total_data_points = len(log_csv) * num_mrs

    percent_violations = (rule_violations.sum() / total_data_points) * 100
    percent_non_violations = 100 - percent_violations

    return {
        'labels': ['Violations', 'Non-violations'],
        'data': [percent_violations, percent_non_violations],
        'total_data_points': total_data_points,
    }
