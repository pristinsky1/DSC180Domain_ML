import sys
import os
import json
sys.path.insert(0, 'src')
from all import features_labels
from all  import ml_model_analysis
from all import input_feature_label
from all import ml_model_train

def main(targets):
    '''
    Given the targets, main runs the main project pipeline logic.
    '''
    
    if 'test' in targets:
        with open('config/test-params.json') as test_params:
            feature_cfg = json.load(test_params)
            
            # make the data target
            file_names, file_labels, new_df = features_labels(**feature_cfg)
            new_df.to_csv("test/output/test_output.csv")
            print("The associated test file names are: ") 
            print(file_names)
            print("The associated test file labels are: ") 
            print(file_labels)
            print("Created the new test features! Check folder test/output/ and observe the output features csv file!")
    return

    if 'result' in targets:
        with open('config/input-params.json') as input_params, open('config/train-data-params.json') as data_params:
            input_cfg = json.load(input_params)
            data_cfg = json.load(data_params)
            
            # make the data target
            data_names, data_labels, data_df = features_labels(**data_cfg)
            input_names, input_labels, input_df = input_feature_label(**input_cfg)
            final_result = ml_model_train(data_df, data_labels, input_df, input_labels)
            print(final_result)
    return

    if 'analysis' in targets:
        with open('config/train-data-params.json') as data_params:
            data_cfg = json.load(data_params)
            
            # make the data target
            data_names, data_labels, data_df = features_labels(**data_cfg)
            prediction_labels, test_labels = ml_model_analysis(data_df, data_labels)
    return

if __name__=='__main__':
    #run via:
    targets = sys.argv[1:]
    main(targets)
