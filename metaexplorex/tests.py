from contextlib import nullcontext
import pytest
from django.urls import reverse
from unittest.mock import patch, MagicMock
import json
import pandas as pd

from metaexplorex.views import convert_json_to_csv_if_needed, get_chart_data, get_chart_data2, get_chart_data3, get_chart_data4, get_chart_data5, get_chart_data6, get_chart_data7

@pytest.mark.django_db
class TestMetaExploreXViews:
    def test_dashboard(self, client):
        response = client.get(reverse('dashboard'), {'num_mrs': '10', 'file_type': 'json', 'selectedFile': '../metaexplorex/expanded_test.json'})
        assert response.status_code == 200
        assert json.loads(response.content) == {'message': 'Data received successfully.'}

    def test_convert_json_to_csv_if_needed(self):
        result = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        assert result is not None
        assert result.endswith('.csv')

    @patch('metaexplorex.views.get_chart_data')
    def test_process_chart_data(self, log_csv, client):
        uploaded_file = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        log_csv = pd.read_csv(uploaded_file, low_memory=False)
        response = client.get(reverse('chart-data'))  
        assert response.status_code == 200
        chart_data = get_chart_data(log_csv)

        assert chart_data['labels'] == [ "MR1_checker", "MR2_checker", "MR3_checker", "MR4_checker", "MR5_checker", "MR6_checker", "MR7_checker", "MR8_checker"]
        assert chart_data['data'] == [0, 0, 102, 74, 0, 109, 99, 0]  

    @patch('metaexplorex.views.get_chart_data2')
    def test_process_chart_data2(self, log_csv, client):
        uploaded_file = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        log_csv = pd.read_csv(uploaded_file, low_memory=False)
        response = client.get(reverse('chart-data2'))  
        assert response.status_code == 200
        chart_data = get_chart_data2(log_csv)

        assert chart_data['labels'] == [ "MR1_checker", "MR2_checker", "MR3_checker", "MR4_checker", "MR5_checker", "MR6_checker", "MR7_checker", "MR8_checker"]
        assert chart_data['data'] == [200, 200, 98, 76, 200, 91, 101, 200]  

    @patch('metaexplorex.views.get_chart_data3')
    def test_process_chart_data3(self, log_csv, client):
        uploaded_file = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        log_csv = pd.read_csv(uploaded_file, low_memory=False)
        response = client.get(reverse('chart-data3'))  
        assert response.status_code == 200
        chart_data = get_chart_data3(log_csv)

        assert chart_data['labels'] == [ "MR1_checker", "MR2_checker", "MR3_checker", "MR4_checker", "MR5_checker", "MR6_checker", "MR7_checker", "MR8_checker"]
        assert chart_data['data'] == [0, 0, 0, 50, 0, 0, 0, 0]  

    @patch('metaexplorex.views.get_chart_data4')
    def test_process_chart_data4(self, log_csv, client):
        uploaded_file = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        log_csv = pd.read_csv(uploaded_file, low_memory=False)
        response = client.get(reverse('chart-data4'))  
        assert response.status_code == 200
        chart_data = get_chart_data4(log_csv)

        assert chart_data['labels'] == [ "MR1_checker", "MR2_checker", "MR3_checker", "MR4_checker", "MR5_checker", "MR6_checker", "MR7_checker", "MR8_checker"]
        assert chart_data['data'] == [200, 200, 200, 150, 200, 200, 200, 200]

    @patch('metaexplorex.views.get_chart_data7')
    def test_process_chart_data7(self, log_csv, client):
        uploaded_file = convert_json_to_csv_if_needed('../metaexplorex/expanded_test.json')
        log_csv = pd.read_csv(uploaded_file, low_memory=False)
        response = client.get(reverse('chart-data7'))  
        assert response.status_code == 200
        chart_data = get_chart_data7(log_csv)

        assert chart_data['labels'] == [ "Violations","Non-violations"]
        assert chart_data['data'] == [24.0, 76.0]
        assert chart_data['total_data_points'] == 1600

    def test_fetch_random_data_api(self, client):
        response = client.get(reverse('fetch-random-data'), {'offset': '0'})  
        assert response.status_code == 200

    def test_fetch_insights_api(self, client):
        response = client.get(reverse('fetch-insights'))  
        assert response.status_code == 200