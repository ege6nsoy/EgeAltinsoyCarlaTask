##OPTION A
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv('/Users/egealtinsoy/my_flask_app/salary_survey-1.csv')
data2 = pd.read_csv('/Users/egealtinsoy/my_flask_app/salary_survey-2.csv')

combined_data = pd.concat([data, data2], ignore_index=True)


##For task3 serializing
#I used https://www.liquid-technologies.com/online-json-to-schema-converter
# for converting JSON to JSON schema
#I pasted 2 dataset and it gave the output which columns to use 
#I pasted some data from dataset1 and dataset2
#which are salary_survey-1.csv and salary_survey-2.csv
#There is 1 common column which is TimeStamp
#But between salary_survey-1.csv and salary_survey-3.csv
#There 2 common columns which are Time stamp and Gender
#Also to discover the datasets I used Google Collab with PYTHON
def serialize_record(record):
    return {
        "timestamp": record.get("Timestamp"),
        "age_range": record.get("How old are you?"),
        "industry": record.get("What industry do you work in?") or record.get("Industry in Company"),
        "job_title": record.get("Job title") or record.get("Job Title In Company"),
        "annual_salary": record.get("What is your annual salary?") or record.get("Total Base Salary in 2018 (in USD)"),
        "currency": record.get("Please indicate the currency"),
        "location": record.get("Where are you located? (City/state/country)") or record.get("Primary Location (Country)"),
        "years_experience": record.get("How many years of post-college professional work experience do you have?") or record.get("Years Experience in Industry"),
        "job_title_context": record.get("If your job title needs additional context, please clarify here:"),
        "other_currency": record.get('If "Other," please indicate the currency here: '),
        "employment_type": record.get("Employment Type"),
        "company_name": record.get("Company Name"),
        "company_size": record.get("Company Size - # Employees"),
        "city": record.get("Primary Location (City)"),
        "company_type": record.get("Public or Private Company"),
        "years_in_company": record.get("Years of Experience in Current Company"),
        "job_ladder": record.get("Job Ladder"),
        "job_level": record.get("Job Level"),
        "required_hours_per_week": record.get("Required Hours Per Week"),
        "actual_hours_per_week": record.get("Actual Hours Per Week"),
        "education_level": record.get("Highest Level of Formal Education Completed"),
        "total_bonus": record.get("Total Bonus in 2018 (cumulative annual value in USD)"),
        "total_equity": record.get("Total Stock Options/Equity in 2018 (cumulative annual value in USD)"),
        "health_insurance": record.get("Health Insurance Offered"),
        "annual_vacation": record.get("Annual Vacation (in Weeks)"),
        "job_satisfaction": record.get("Are you happy at your current position?"),
        "resignation_plan": record.get("Do you plan to resign in the next 12 months?"),
        "industry_opinion": record.get("What are your thoughts about the direction of your industry?"),
        "gender": record.get("Gender"),
        "top_skills": record.get("Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?"),
        "bootcamp_experience": record.get("Have you ever done a bootcamp? If so was it worth it?")
    }

#main domain to test on local server I see the hello flask on
#http://XXX.X.X.X:5000
@app.route('/')
def home():
    return 'Hello, Flask!'
#http://127.0.0.1:5000/composition_data for this route
@app.route('/compensation_data/<timestamp>', methods=['GET'])
def get_single_record(timestamp):
    # Filter data by Timestamp
    record = combined_data[combined_data['Timestamp'] == timestamp]
    
    # Handle sparse fieldsets
    fields = request.args.get('fields')
    if fields:
        field_list = fields.split(',')
        record = record[field_list]

    if record.empty:
        return jsonify({'error': 'Record not found'}), 404
    else:
        serialized_record = serialize_record(record.iloc[0].to_dict())
        return jsonify(serialized_record)

@app.route('/compensation_data', methods=['GET'])
def get_compensation_data():
    query = request.args
    filtered_data = combined_data
    #For filtering and sorting in some cases queries from postman
    #works with normal version in some cases the encoded version works
    # Filtering logic
    for key, value in query.items():
        if key not in ['sort', 'order', 'fields']:
            filtered_data = filtered_data[filtered_data[key] == value]

    # Sorting
    sort_key = request.args.get('sort')
    if sort_key:
        sort_order = request.args.get('order', 'asc')  # Default to ascending
        filtered_data = filtered_data.sort_values(by=sort_key, ascending=(sort_order == 'asc'))

    # Sparse fieldsets
    fields = request.args.get('fields')
    if fields:
        field_list = fields.split(',')
        filtered_data = filtered_data[field_list]

    serialized_data = [serialize_record(record) for record in filtered_data.to_dict(orient='records')]
    return jsonify(serialized_data)

if __name__ == '__main__':
    app.run(debug=True)
'''
THE WORKING OF SORT AND FILTER AND SPARSE FIELDSET ; AFTER NORMALIZED MIXED
Unfourtunately forgot to save but have screenshots

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv('/Users/egealtinsoy/my_flask_app/salary_survey-1.csv')

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/compensation_data', methods=['GET'])
def get_compensation_data():
    job_title = request.args.get('Job title')
    sort_key = request.args.get('sort')
    sort_order = request.args.get('order', 'asc')  # Default to ascending

    # Filter data based on the job title if provided
    if job_title:
        filtered_data = data[data['Job title'] == job_title]
    else:
        filtered_data = data

    # Sort data if sort key is provided
    if sort_key:
        filtered_data = filtered_data.sort_values(by=sort_key, ascending=(sort_order == 'asc'))

    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/compensation_data/<int:id>', methods=['GET'])
def get_single_record(id):
    record = data[data['id'] == id]
    return jsonify(record.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)



'''