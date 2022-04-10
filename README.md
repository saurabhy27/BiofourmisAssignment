Steps:

1. Download and Install Python (version >= 3.6)
2. Run <i>pip install requirements.txt</i>
3. Run the project <i>python main.py</i>
4. When you will run the command the server will start. This server has two APIs
    1. Insert wearable data into input.csv file
    2. Return the aggregated response
5. To insert the data run generate_value file which will generate the random value and call the insert API. This will
   run for 60 minutes.
6. To see the Aggregated report Hit the Output API.

API Description:

1. Insert API
    1. Method <i>POST</i>
    2. URL <i>BASE_URL + /vitals_input</i>
    3. Json <code>{"user_id" : "abc", "timestamp" : 1587631419, "heart_rate" : 45,
       "respiration_rate" : 18, “activity": 3}</code>
2. Output API
    1. Method <i>GET</i>
    2. URL <i>BASE_URL + /vitals_output/<min></i>