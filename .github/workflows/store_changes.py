import os
import json


def storeForecasts (forecasts):

    team = os.path.basename(os.path.split(forecasts[0])[0]).split('-')[0]
    if not team:
     raise Exception(f"invalid input data  {forecasts}\n")

    out_data = {}    
    out_data['team'] = team
    out_data['models'] = []

    for forecast in forecasts:

        #get the model name from path
        model = tuple(os.path.basename(os.path.split(forecast)[0]).split('-'))[1]

        model_entry = next((item for item in out_data['models'] if item["model"] == model), None)
        if model_entry is None:
            out_data['models'].append({"model" : model, "changes": [forecast]})
        else:
            model_entry["changes"].append(forecast)

    if out_data['models']:
        print(f"Current path: {os.getcwd()}")
        # db_path = os.path.join("..", "data-storage", "changes_db.json")
        db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data-storage", "changes_db.json")
        updateForecastsJson(db_path, out_data)
    

def updateForecastsJson(json_file_path, changes):

    json_data = None

    team = changes.get("team")
    n_entries = changes.get("models")

    # Step 1: Read the existing data from the JSON file
    try:
        with open (json_file_path, 'r') as fdb:
            json_data = json.load(fdb)
            print(f"JSON FORECASTS CONTENT: \n{json_data}")
            
    except FileNotFoundError:
        # If the file doesn't exist, handle error
        raise Exception(f"Json file not found {json_file_path}\n")

    # Check if the "team" key exists and is a list
    if team not in json_data:
        # if brand new, just save commits
        json_data[team] = n_entries

    else:
        #get the list of previous saved data for this team
        j_records = json_data[team]

        for entry in n_entries:
                
            j_model = [j_record for j_record in j_records if j_record.get("model") == entry.get("model")]
            if j_model == [] :
                j_records.append(entry)
                print("Add new team to the backup")
            else:
                j_model[0]["changes"] += set(entry["changes"]).difference (j_model[0]["changes"])

    

    try:
        with open(json_file_path, 'w') as fdb:
            print(f"Saving json: \n{json_data}")
            json.dump(json_data, fdb, indent=4)
    except:
        # If the file doesn't exist, handle error
        raise Exception(f"Error writing  {json_data} \n to json file: {json_file_path}\n")
    
    
    print(f"JOB DONE updateForecastsJson >>>>>>>>")




def storetMetaData (metadata):
    print ("Storing meta-data")
    db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data-storage", "metadata_db.json")
    updateMetadataJson(db_path, metadata)


def updateMetadataJson (json_file_path, changes):

    json_data = None

    # Step 1: Read the existing data from the JSON file
    try:
        with open (json_file_path, 'r') as fdb:
            json_data = json.load(fdb)
            print(f"JSON METADATA CONTENT: \n{json_data}")
            
    except FileNotFoundError:
        # If the file doesn't exist, handle error
        raise Exception(f"Json file not found {json_file_path}\n")

    json_data["changes"] = changes if "changes" not in json_data else  list(set(json_data["changes"] + changes))

    try:
        with open(json_file_path, 'w') as fdb:
            json.dump(json_data, fdb, indent=4)
            print(f"Saving json: \n{json_data}")
    except:
        # If the file doesn't exist, handle error
        raise Exception(f"Error writing  {json_data} \n to json file: {json_file_path}\n")

    print(f"JOB DONE updateMetadataJson >>>>>>>>")

###
###
def store(to_store):

    print(f"Store -> {to_store}")
    
    # Make a list out of the changed files
    fchanges = to_store.split(" ")

    # List should not be empty
    if not fchanges:
        raise Exception(f"Empty commit")
    

    model_changes = []
    metadata_changes = []
    
    # 
    for fchanged in fchanges:
                
        # get type from path
        path_split = os.path.split(fchanged)
        dirname = os.path.dirname(path_split[0])

        # needed for different deepness of paths
        rootFolder = dirname if dirname != '' else path_split[0]
        if rootFolder == "model-output":
            # save model output
            model_changes.append(fchanged)
        elif rootFolder == "model-metadata":
            # save meta-data
            metadata_changes.append(fchanged)
        else :
            # unknown just discard
            print (f'Unkown file submitted {rootFolder}! Skip it')


    if model_changes:
        storeForecasts(model_changes)

    if metadata_changes:
        storetMetaData(metadata_changes)



if __name__ == "__main__":
    # store_data = 'model-metadata/ISI-AutoArima.yml model-metadata/ISI-Test1.yml model-output/Test1-SIRModel/2023-11-04-Test1-SIRModel.csv model-output/Test1-SIRModel/2023-11-05-Test1-SIRModel.csv model-output/Test1-SIRModel/2023-11-06-Test1-SIRModel.csv'
    store_data = os.getenv("data")        

    store(store_data)
