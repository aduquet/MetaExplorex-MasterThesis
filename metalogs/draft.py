from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

def metalogs(request):
    missing_columns_str = None
    chart_data = None  
    chart_data2 = {'labels': [], 'data': []}  
    chart_data3 = None
    chart_data3_list = []

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']

        try:
            log_csv = pd.read_csv(uploaded_file)

            is_multiple_type = request.POST.get('analysis_option') == 'multiple'

            all_columns = log_csv.columns

            output_columns = ['output_testInput']
            mrs_output_columns = []
            mrs_checker_columns = []

            for column in all_columns:
                if column.startswith('output_MR'):
                    mrs_output_columns.append(column)
                elif column.endswith('_checker'):
                    mrs_checker_columns.append(column)

            required_columns = output_columns + mrs_output_columns + mrs_checker_columns

            missing_columns = [col for col in required_columns if col not in log_csv.columns]

            if missing_columns:
                missing_columns_str = ', '.join(missing_columns)
                return JsonResponse({'error': f'Missing columns in log file: {missing_columns_str}'}, status=400)

            rule_violations = log_csv[required_columns[7:]].apply(lambda x: (x == 'Violated').sum())

            chart_data = {
                'labels': required_columns[7:],
                'data': rule_violations.tolist(),
            }

            checker_columns = ['MR1_checker', 'MR2_checker', 'MR3_checker', 'MR4_checker', 'MR5_checker', 'MR6_checker']
            crashed_rows = log_csv[checker_columns].apply(lambda x: x[~x.isin(['Violated', 'Not-violated'])].count())

            for column, count in zip(checker_columns, crashed_rows):
                chart_data2['labels'].append(column)
                chart_data2['data'].append(count)

            for idx, column in enumerate(required_columns[7:]):
                rule_name = column.replace("_checker", "")
                violated_rows = log_csv[log_csv[column] == 'Violated']

                output_column = f'output_{rule_name}'
                cleaned_values = violated_rows[output_column].apply(pd.to_numeric, errors='coerce').dropna()
                
                if not cleaned_values.empty:
                    chart_data3_list.append({
                        'label': f'{output_column} for {rule_name} Violations',
                        'data': cleaned_values.tolist(),
                        'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                        'borderColor': 'rgba(255, 99, 132, 1)',
                        'borderWidth': 1,
                    })

            chart_data3 = {
                'labels': [item['label'] for item in chart_data3_list],
                'datasets': chart_data3_list,
            }

            return render(request, 'metalogs/metalogs.html', {
                'missing_columns': missing_columns_str,
                'chart_data': chart_data,  
                'chart_data2': chart_data2,
                'chart_data3': chart_data3,
            })

        except Exception as e:
            return JsonResponse({'error': f'Error processing file: {str(e)}'}, status=400)

    return render(request, 'metalogs/metalogs.html', {
        'missing_columns': missing_columns_str,
        'chart_data': chart_data,  
        'labels': chart_data['labels'] if chart_data else [], 
        'chart_data2': chart_data2,
        'chart_data3': chart_data3,
    })
