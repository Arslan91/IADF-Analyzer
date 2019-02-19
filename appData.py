import os
import csv

def app_data(f):
    # Search Strings (Features to extract)
    search_package = 'package'
    search_intent = 'Intent('
    search_action = 'setAction('
    search_class = 'setClass('
    search_className = 'setClassName('
    search_component = 'setComponent('
    search_data = 'setData('
    search_data_normalize = 'setDataAndNormalize('
    search_data_and_type = 'setDataAndType('
    search_data_type_normalize = 'setDataAndTypeAndNormalize('
    search_extra_class_loader = 'setExtrasClassLoader('
    search_data_type = 'setType('
    search_type_normalize = 'setTypeAndNormalize('
    search_category = 'addCategory('
    search_extras = 'putExtra('
    search_set_flags = 'setFlags('
    search_set_package = 'setPackage('
    search_add_flags = 'addFlags('
    search_int_arr_extra = 'putIntegerArrayListExtra('
    search_str_arr_extra = 'putStringArrayListExtra('
    search_parse_list_extra = 'putParcelableArrayListExtra('

    search_startActivity = 'startActivity'
    search_startActivityForResult = 'startActivityForResult'
    search_sendBroadcast = 'sendBroadcast'
    search_startService = 'startService'

    csv_file = os.path.isfile('./output/data.csv')

    # for root, dirs, files in os.walk('./decompiled_apps/'):
    #     for name in files:
    #         path = os.path.join(root, name)
    #         if path.endswith('.java'):
    with open(f) as file:

        package = ''

        name = file.name.split('/')
        activityName = name[-1].replace('.java', '')

        # CSV file headers
        f = open('./output/data.csv', 'a')
        headers = ['Package', 'Activity', 'Intent', 'Context', 'Class', 'String', 'Uri', 'Action', 'Category',
                   'Class Context', 'packageName', 'packageContext', 'packageClass', 'Component', 'Data Uri', 'MIME Type',
                   'Class Loader', 'Extras Intent', 'Extras Bundle', 'Extras String', 'Extras Value', 'Flags',
                   'Activity Type']
        headers_writer = csv.DictWriter(f, fieldnames=headers)

        if not csv_file:
            headers_writer.writeheader()

        for line in file:

            # initializing variables
            intent = ''
            context = ''
            intentClass = ''
            string = ''
            intentUri = ''
            intentAction = ''
            intentCategory = ''
            intentClassContext = ''
            packageName = ''
            packageContext = ''
            packageClass = ''
            intentComponent = ''
            intentData = ''
            intent_data_normalize = ''
            intentDataUri = ''
            intentMIMEType = ''
            intentExtraClass = ''
            ExtrasIntent = ''
            ExtrasBundle = ''
            ExtrasString = ''
            ExtrasValue = ''
            intentFlags = ''
            activity = ''

            # Matching and extracting features
            if search_package in line:
                package_name = line[line.find(search_package)+len(search_package):-2]
                package = package_name.replace(' ', '')

            if search_intent in line:
                intent_argus = line[line.find(search_intent)+len(search_intent):].split(",")
                if len(intent_argus) == 0:
                    intent = 'Implicit'
                elif len(intent_argus) == 1:
                    if 'Intent' in intent_argus[0]:
                        intent = intent_argus[0].replace('(Intent)', '').replace(')', '').replace(';', '').strip()
                    else:
                        context = intent_argus[0].replace('(Context)', '').replace(')', '').replace(';', '').strip()
                elif len(intent_argus) == 2:
                    if 'String' in intent_argus[0]:
                        string = intent_argus[0].replace('(String)', '').replace(')', '').replace(';', '').strip()
                    else:
                        context = intent_argus[0].replace('(Context)', '').replace(')', '').replace(';', '').strip()

                    if 'Uri' in intent_argus[1]:
                        intentUri = intent_argus[1].replace('(Uri)', '').replace(')', '').replace(';', '').strip()
                    else:
                        intentClass = intent_argus[1].replace('(Class)', '').replace(')', '').replace(';', '').strip()
                elif len(intent_argus) == 4:
                    string = intent_argus[0].replace('(String)', '').replace(')', '').replace(';', '').strip()
                    intentUri = intent_argus[0].replace('(Uri)', '').replace(')', '').replace(';', '').strip()
                    context = intent_argus[0].replace('(Context)', '').replace(')', '').replace(';', '').strip()
                    intentClass = intent_argus[0].replace('(Class)', '').replace(')', '').replace(';', '').strip()
                else:
                    intent = intent_argus[0].replace(')', '').replace(';', '').strip()
                    intentClass = intent_argus[1].replace(')', '').replace(';', '').strip()

            elif search_action in line:
                intent_action = line[line.find(search_action)+len(search_action):].split(',')
                intentAction = intent_action[0].replace(')', '').replace(';', '').strip()

            elif search_class in line:
                intent_class = line[line.find(search_class)+len(search_class):].split(',')
                intentClassContext = intent_class[0].replace(')', '').replace(';', '').strip()
                intentClass = intent_class[0].replace(')', '').replace(';', '').strip()

            elif search_className in line:
                intent_className = line[line.find(search_className)+len(search_className):].split(',')
                if 'string' in intent_className[0]:
                    packageName = intent_className[0].replace(')', '').replace(';', '').strip()
                else:
                    packageContext = intent_className[0].replace(')', '').replace(';', '').strip()
                packageClass = intent_className[0].replace(')', '').replace(';', '').strip()

            elif search_component in line:
                intent_component = line[line.find(search_component)+len(search_component):].split(',')
                intentComponent = intent_component[0].replace(')', '').replace(';', '').strip()

            elif search_data in line:
                intent_data = line[line.find(search_data)+len(search_data):].split(',')
                intentData = intent_data[0].replace(')', '').replace(';', '').strip()

            elif search_data_normalize in line:
                intent_data_normalize = line[line.find(search_data_normalize)+len(search_data_normalize):].split(',')
                intentData = intent_data_normalize[0].replace(')', '').replace(';', '').strip()

            elif search_data_and_type in line:
                intent_data_and_type = line[line.find(search_data_and_type)+len(search_data_and_type):].split(',')
                intentData = intent_data_and_type[0].replace(')', '').replace(';', '').strip()
                intentMIMEType = intent_data_and_type[1].replace(')', '').replace(';', '').strip()

            elif search_data_type_normalize in line:
                intent_data_and_type = line[line.find(search_data_type_normalize)+len(search_data_type_normalize):].split(',')
                intentData = intent_data_and_type[0].replace(')', '').replace(';', '').strip()
                intentMIMEType = intent_data_and_type[1].replace(')', '').replace(';', '').strip()

            elif search_extra_class_loader in line:
                intent_extraClass = line[line.find(search_extra_class_loader)+len(search_extra_class_loader):].split(',')
                intentExtraClass = intent_extraClass[0].replace(')', '').replace(';', '').strip()

            elif search_data_type in line:
                intent_dataType = line[line.find(search_data_type)+len(search_data_type):].split(',')
                intentMIMEType = intent_dataType[0].replace(')', '').replace(';', '').strip()

            elif search_type_normalize in line:
                intent_dataTypeNormalize = line[line.find(search_type_normalize)+len(search_type_normalize):].split(',')
                intentMIMEType = intent_dataTypeNormalize[0].replace(')', '').replace(';', '').strip()

            elif search_category in line:
                intent_category = line[line.find(search_category)+len(search_category):].split(',')
                intentCategory = intent_category[0].replace(')', '').replace(';', '').strip()

            elif search_extras in line:
                intent_extra = line[line.find(search_extras)+len(search_extras):].split(',')
                if len(intent_extra) == 1:
                    if 'Intent' in intent_extra:
                        ExtrasIntent = intent_extra[0].replace(')', '').replace(';', '').strip()
                    else:
                        ExtrasBundle = intent_extra[0].replace(')', '').replace(';', '').strip()
                else:
                    ExtrasString = intent_extra[0].replace(')', '').replace('"', '').replace(';', '').strip()
                    ExtrasValue = intent_extra[1].replace(')', '').replace(';', '').strip()

            elif search_set_flags in line:
                intent_flags = line[line.find(search_set_flags)+len(search_set_flags):].split(',')
                intentFlags = intent_flags[0].replace(')', '').replace(';', '').strip()

            elif search_set_package in line:
                intent_flags = line[line.find(search_set_package)+len(search_set_package):].split(',')
                intentFlags = intent_flags[0].replace(')', '').replace(';', '').strip()

            elif search_add_flags in line:
                intent_flags = line[line.find(search_add_flags)+len(search_add_flags):].split(',')
                intentFlags = intent_flags[0].replace(')', '').replace(';', '').strip()

            elif search_startActivity in line:
                activity = 'Activity'

            elif search_startActivityForResult in line:
                activity = 'Activity for result'

            elif search_sendBroadcast in line:
                activity = 'Broadcast'

            elif search_startService in line:
                activity = 'Service'

            else:
                pass

            # Writing Data to CSV
            # ===================

            if intent or context or intentClass or string or intentUri or intentAction or intentClassContext or packageName \
                    or packageContext or packageClass or intentComponent or intentData or intentMIMEType or intentCategory \
                    or ExtrasIntent or ExtrasBundle or ExtrasString or ExtrasValue or intentFlags or activity:
                field_name = ['Package', 'Activity', 'Intent', 'Context', 'Class', 'String', 'Uri', 'Action', 'Category',
                              'Class Context', 'packageName', 'packageContext', 'packageClass', 'Component', 'Data Uri',
                              'MIME Type', 'Class Loader', 'Extras Intent', 'Extras Bundle', 'Extras String',
                              'Extras Value', 'Flags', 'Activity Type']

                writer = csv.DictWriter(f, fieldnames=field_name)
                writer.writerow({'Package': package, 'Activity': package + '.' + activityName, 'Intent': intent,
                                 'Context': context, 'Class': intentClass, 'String': string, 'Uri': intentUri,
                                 'Action': intentAction, 'Category': intentCategory, 'Class Context': intentClassContext,
                                 'packageName': packageName, 'packageContext': packageContext, 'packageClass': packageClass,
                                 'Component': intentComponent, 'Data Uri': intentData, 'MIME Type': intentMIMEType,
                                 'Class Loader': intentExtraClass, 'Extras Intent': ExtrasIntent,
                                 'Extras Bundle': ExtrasBundle, 'Extras String': ExtrasString, 'Extras Value': ExtrasValue,
                                 'Flags': intentFlags, 'Activity Type': activity})

        f.close()
    return
