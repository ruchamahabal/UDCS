
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile

def read_file(filename, names):
    df = pandas.read_excel(filename, names=names)
    return df 

def clean_datasets(datasets):
    for dataset in datasets.values():
        for i in range(len(dataset)):
            dataset[i] = dataset[i].strip()
            dataset[i] = dataset[i].lower()
    return datasets

def check_exists(word, indices, dataset):
    sub_word = ''
    for index in indices:
        #-1 because indexing starts from 0
        if int(index)<0:
            sub_word += word[int(index)]
        else:
            sub_word += word[(int(index))-1]
    if sub_word in dataset:
        return True
    else:
        return False
        
def get_answer(main_dataset, conditions, datasets):
    for word in main_dataset:
        print(word)
        for condition in conditions:
            print('====d', datasets.get(condition.get('dataset')))
            exists = check_exists(word, condition.get('indices'), datasets.get(condition.get('dataset')))
            if not exists:
                break
        if exists:
            answer = word 
            return answer      

'''main dataset'''
main_dataset_name = input('Enter your main dataset name:')
main_dataset = read_file(main_dataset_name, names=['main'])
main_dataset = main_dataset['main'].tolist()
for i in range(len(main_dataset)):
    main_dataset[i] = main_dataset[i].strip()
    main_dataset[i] = main_dataset[i].lower()

no_of_datasets = int(input('Enter the number of helper datasets:'))
print(no_of_datasets)

'''helper dataset'''
datasets = {}
filenames = []
for i in range(no_of_datasets):
    filename = input('Enter the dataset ' + str(i) + ' name:')
    filenames.append(filename)
    dataset = read_file(filename, names = [filename])
    datasets[filename] = dataset[filename].tolist()
datasets = clean_datasets(datasets)

'''conditions'''
no_of_conditions = int(input('Enter the number of conditions'))
conditions = []
for i in range(no_of_conditions):
    indices = input('Enter all indices separated by commas:').split(',')
    dataset = input('Enter the dataset filename:')
    conditions.append({'indices': indices, 'dataset': dataset})

print(conditions)

answer = get_answer(main_dataset, conditions, datasets)
print('Answer is:',answer)