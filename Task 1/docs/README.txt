Kibana Dashboard: Website Logs Analysis
===================================================================================

Purpose of Dashboard : 

This dashboard utilizes sample data from the perspective of an analyst examining website logs. It aims to provide insights into website traffic, user behavior, and resource usage over time.

===================================================================================

Data Source : The dashboard is built using the "Kibana Sample Data Logs" provided by         	      Kibana.

===================================================================================

Instructions to Build Dashboard

1) Adding Sample Data
  - On the home page, click on "Try sample data."
  - Navigate to "Other sample data sets."
  - Click on the "Sample web logs" card, then click "Add data."
  - Creating the Dashboard
  - Go to the main menu and click on "Dashboard" under Analytics.
  - Click on "Create Visualization" to start building visualizations.
  - Set the time filter to "Last 90 days" to analyze recent data.
  - Ensure that the "Kibana Sample Data Logs" data view is selected.

2) Utilize the following fields for visualization:
  - Records
  - timestamp
  - bytes
  - clientip
  - referer.keyword

3) Visualizations
  - Unique Client IPs Metric: 
	Displays the unique number of client IPs using the Metric visualization type.

  - Bytes Line Chart: 
	Illustrates the change in median bytes over time using a Line Chart.

  - Top Website Requests Table: 
	Presents the most frequent website request values, ranked by unique visitors, 	using a Table visualization.

  - Bytes Distribution Pie Chart: 
	Compares bytes transferred from documents under 10KB versus documents over 	10KB using a Pie Chart.

  - Website Traffic per Hour: 
	Analyzes website traffic trends per hour to identify optimal times for 	routine maintenance using a Bar Vertical Stack visualization.

  - Traffic Sources and Geography Tree Map: 
	Visualizes website traffic sources and user geography using a Tree Map.
	Arranging the Dashboard

4) And finally resize and move panels to ensure all visualizations are displayed without scrolling. And Save the dashboard for future reference.

===================================================================================

Dependencies and Prerequisites :
Download and extract the Elasticsearch and Kibana zip files.
Start Elasticsearch and Kibana (respectively).