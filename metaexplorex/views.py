from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChartDataSerializer
import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class DashboardView(APIView):
    def post(self, request, *args, **kwargs):
        num_mrs = request.data.get('num_mrs') 
        file_type = request.data.get('file_type')


        request.num_mrs = num_mrs
        request.file_type = file_type
        
        print(num_mrs, file_type)
        return JsonResponse({'message': 'Data received successfully.'})
    
@api_view(['GET', 'POST'])
def process_chart_data(request, get_chart_data_func):
    try:
        # num_mrs = request.data.get('num_mrs')
        # file_type = request.data.get('file_type')
        num_mrs = 8
        file_type = 'single'

        if num_mrs is None:
            return Response({'error': 'Number of MRs is missing.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # uploaded_file = request.data.get('file')
        uploaded_file = 'C:/Users/Murad/Desktop/Django_apps/metaexplorex/test.csv'
        print("2", num_mrs, file_type, uploaded_file)
        if not uploaded_file:
            return Response({'error': 'No file uploaded.'}, status=status.HTTP_400_BAD_REQUEST)
        
        log_csv = pd.read_csv(uploaded_file)
        is_multiple_type = file_type == 'multiple'
        missing_columns = get_missing_columns(log_csv, is_multiple_type, int(num_mrs))

        if missing_columns:
            return Response({'error': f'Missing columns in log file: {", ".join(missing_columns)}'}, status=status.HTTP_400_BAD_REQUEST)
        
        chart_data = get_chart_data_func(log_csv)
        serializer = ChartDataSerializer(chart_data)
        return Response(serializer.data)

    except pd.errors.EmptyDataError as e:
        return Response({'error': 'The uploaded file is empty or in an unsupported format.'}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': 'Something went wrong. Check your file and try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET'])
def chart_data_api(request):
    return process_chart_data(request, get_chart_data)

# @api_view(['GET'])
def chart_data2_api(request):
    return process_chart_data(request, get_chart_data2)

# @api_view(['GET'])
def chart_data3_api(request):
    return process_chart_data(request, get_chart_data3)

# @api_view(['GET'])
def chart_data4_api(request):
    return process_chart_data(request, get_chart_data4)


# @api_view(['GET'])
def chart_data5_api(request):
    return process_chart_data(request, get_chart_data5)

# @api_view(['GET'])
def chart_data6_api(request):
    return process_chart_data(request, get_chart_data6)

# @api_view(['GET'])
def chart_data7_api(request):
    return process_chart_data(request, get_chart_data7)

@api_view(['GET'])
def fetch_random_data_api(request):
    try:
        uploaded_file = 'C:/Users/Murad/Desktop/Django_apps/metaexplorex/test.csv'
        log_csv = pd.read_csv(uploaded_file)
        # Get the offset from request query parameters, default to 0 if not provided
        offset = int(request.query_params.get('offset', 0))
        # Call fetchRandomData with the offset
        random_data = fetchRandomData(log_csv, offset=offset)
        return JsonResponse({'random_data': random_data})
    except pd.errors.EmptyDataError as e:
        return Response({'error': 'The uploaded file is empty or in an unsupported format.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': 'Something went wrong. Check your file and try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_missing_columns(log_csv, is_multiple_type, num_mrs):
    all_columns = log_csv.columns

    if len(all_columns) == 3 * num_mrs + 3:
        if is_multiple_type:
            required_columns = ['output_testInput', 'output_MR', 'MR_checker']
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

    labels = checker_columns.tolist()
    data = rule_violations.tolist()

    chart_data = {
        'labels': labels,
        'data': data,
        'input_testData_with_violations': input_testData_with_violations,
        'violated_MRchecker': violated_MRchecker,
        'output_testInput': output_testInput
    }

    return chart_data

def get_chart_data2(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    rule_violations = log_csv[checker_columns].apply(lambda x: (x == 'Not-violated').sum())
    labels = checker_columns.tolist()
    data = rule_violations.tolist()

    chart_data = {
        'labels': labels,
        'data': data
    }

    return chart_data

def get_chart_data3(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    crashed_rows = log_csv[checker_columns].apply(lambda x: x[~x.isin(['Violated', 'Not-violated'])].count())
    labels = checker_columns.tolist()
    data = crashed_rows.tolist()
    
    chart_data = {
        'labels': labels, 
        'data': data
    }
    return chart_data

def get_chart_data4(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    not_crashed_rows = log_csv[checker_columns].apply(lambda x: x[x.isin(['Violated', 'Not-violated'])].count())
    labels = checker_columns.tolist()
    data = not_crashed_rows.tolist()
    
    chart_data = {
        'labels': labels, 
        'data': data
    }
    return chart_data


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
    data = chart_data5_list

    chart_data = {
        'labels': labels, 
        'data': data
    }
    return chart_data

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
    data = chart_data_list

    chart_data = {
        'labels': labels, 
        'data': data
    }
    return chart_data


def get_chart_data7(log_csv):
    checker_columns = log_csv.filter(like='_checker').columns
    num_mrs = len(checker_columns)
    rule_violations = log_csv[checker_columns].apply(lambda x: (x == 'Violated').sum())
    total_data_points = len(log_csv) * num_mrs

    percent_violations = (rule_violations.sum() / total_data_points) * 100
    percent_non_violations = 100 - percent_violations

    labels = ['Violations', 'Non-violations']
    data = [percent_violations, percent_non_violations]
    
    chart_data = {
        'labels': labels, 
        'data': data,
        'total_data_points': total_data_points,
    }
    return chart_data


def fetchRandomData(log_csv, offset=0, limit=50):
    # Calculate the end index based on the offset and limit
    end = offset + limit
    if len(log_csv) >= 50:
        random_data = log_csv.sample(n=50).to_dict('records')
    else:
        random_data = log_csv.to_dict('records')
    return random_data
