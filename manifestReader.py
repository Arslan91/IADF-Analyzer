import os
from bs4 import BeautifulSoup
import csv


def manifest_reader(file):
    csv_file = os.path.isfile('./output/manifest.csv')

    with open(f'./decompiled_apps/{file}') as file:
        soup = BeautifulSoup(file, 'xml')

    with open('./output/manifest.csv', 'a', newline='') as file:
        headers = ['Package', 'Activity', 'Exported', 'Permission', 'Action', 'Category', 'MimeType',
                   'Scheme', 'Host', 'Port', 'Path']
        headers_writer = csv.DictWriter(file, fieldnames=headers)

        if not csv_file:
            headers_writer.writeheader()

        package_name = soup.manifest['package']

        # Activity Data
        # =============
        for activity in soup.find_all('activity'):
            if 'android:name' in activity.attrs:
                activity_name = activity['android:name']

            if 'android:exported' in activity.attrs:
                activity_exported = activity['android:exported']
            else:
                activity_exported = 'false'

            if 'android:permission' in activity.attrs:
                activity_permission = activity['android:permission']
            else:
                activity_permission = 'None'

            # if intent-filter is not configured
            if not activity.find('intent-filter'):

                field_name = ['Package', 'Activity', 'Exported', 'Permission']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported,
                                 'Permission': activity_permission})

            else:
                # action = ''
                category = ''
                mimeType = ''
                data_scheme = ''
                data_host = ''
                data_port = ''
                data_path = ''
                data_pathPattern = ''
                data_pathPrefix = ''

                for intent in activity.find_all('intent-filter'):
                    for action in intent.find_all('action'):
                        if 'android:name' in action:
                            action = action['android:name']

                    if intent.find('category'):
                        for category in intent.find_all('category'):
                            if 'android:name' in category:
                                category = category['android:name']

                    if intent.find('data'):
                        for data in intent.find_all('data'):
                            if 'android:mimeType' in data.attrs:
                                mimeType = data['android:mimeType']

                            if 'android:scheme' in data.attrs:
                                data_scheme = data['android:scheme']

                            if 'android:host' in data.attrs:
                                data_host = data['android:host']

                            if 'android:port' in data.attrs:
                                data_port = data['android:port']

                            if 'android:path' in data.attrs:
                                data_path = data['android:path']

                            if 'android:pathPattern' in data.attrs:
                                data_pathPattern = data['android:pathPattern']

                            if 'android:pathPrefix' in data.attrs:
                                data_pathPrefix = data['android:pathPrefix']

                field_name = ['Package', 'Activity', 'Exported', 'Permission', 'Action', 'Category', 'MimeType',
                              'Scheme', 'Host', 'Port', 'Path']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported, 'Permission': activity_permission,
                                 'Action': action, 'Category': category,
                                 'MimeType': mimeType, 'Scheme': data_scheme, 'Host': data_host,
                                 'Port': data_port, 'Path': data_path+data_pathPattern+data_pathPrefix})

        # Service Data
        # =============

        for service in soup.find_all('service'):
            if 'android:name' in service:
                activity_name = service['android:name']

            if 'android:exported' in service.attrs:
                activity_exported = service['android:exported']
            else:
                activity_exported = 'false'

            if 'android:permission' in service.attrs:
                activity_permission = service['android:permission']
            else:
                activity_permission = 'None'

            # if intent-filter is not configured
            if not service.find('intent-filter'):

                field_name = ['Package', 'Activity', 'Exported', 'Permission']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported,
                                 'Permission': activity_permission})

            else:
                action = ''
                category = ''
                mimeType = ''
                data_scheme = ''
                data_host = ''
                data_port = ''
                data_path = ''
                data_pathPattern = ''
                data_pathPrefix = ''

                for intent in service.find_all('intent-filter'):
                    for action in intent.find_all('action'):
                        if 'android:name' in action:
                            action = action['android:name']

                    if intent.find('category'):
                        for category in intent.find_all('category'):
                            category = category['android:name']

                    if intent.find('data'):
                        for data in intent.find_all('data'):
                            if 'android:mimeType' in data.attrs:
                                mimeType = data['android:mimeType']

                            if 'android:scheme' in data.attrs:
                                data_scheme = data['android:scheme']

                            if 'android:host' in data.attrs:
                                data_host = data['android:host']

                            if 'android:port' in data.attrs:
                                data_port = data['android:port']

                            if 'android:path' in data.attrs:
                                data_path = data['android:path']

                            if 'android:pathPattern' in data.attrs:
                                data_pathPattern = data['android:pathPattern']

                            if 'android:pathPrefix' in data.attrs:
                                data_pathPrefix = data['android:pathPrefix']

                field_name = ['Package', 'Activity', 'Exported', 'Permission', 'Action', 'Category', 'MimeType',
                              'Scheme', 'Host', 'Port', 'Path']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported, 'Permission': activity_permission,
                                 'Action': action, 'Category': category,
                                 'MimeType': mimeType, 'Scheme': data_scheme, 'Host': data_host,
                                 'Port': data_port, 'Path': data_path+data_pathPattern+data_pathPrefix})

        # Receiver Data
        # =============

        for receiver in soup.find_all('receiver'):
            if 'android:name' in receiver:
                activity_name = receiver['android:name']

            if 'android:exported' in receiver.attrs:
                activity_exported = receiver['android:exported']
            else:
                activity_exported = 'false'

            if 'android:permission' in receiver.attrs:
                activity_permission = receiver['android:permission']
            else:
                activity_permission = 'None'

            # if intent-filter is not configured
            if not receiver.find('intent-filter'):

                field_name = ['Package', 'Activity', 'Exported', 'Permission']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported,
                                 'Permission': activity_permission})

            else:
                action = ''
                category = ''
                mimeType = ''
                data_scheme = ''
                data_host = ''
                data_port = ''
                data_path = ''
                data_pathPattern = ''
                data_pathPrefix = ''

                for intent in receiver.find_all('intent-filter'):
                    for action in intent.find_all('action'):
                        if 'android:name' in action:
                            action = action['android:name']

                    if intent.find('category'):
                        for category in intent.find_all('category'):
                            category = category['android:name']

                    if intent.find('data'):
                        for data in intent.find_all('data'):
                            if 'android:mimeType' in data.attrs:
                                mimeType = data['android:mimeType']

                            if 'android:scheme' in data.attrs:
                                data_scheme = data['android:scheme']

                            if 'android:host' in data.attrs:
                                data_host = data['android:host']

                            if 'android:port' in data.attrs:
                                data_port = data['android:port']

                            if 'android:path' in data.attrs:
                                data_path = data['android:path']

                            if 'android:pathPattern' in data.attrs:
                                data_pathPattern = data['android:pathPattern']

                            if 'android:pathPrefix' in data.attrs:
                                data_pathPrefix = data['android:pathPrefix']

                field_name = ['Package', 'Activity', 'Exported', 'Permission', 'Action', 'Category', 'MimeType',
                              'Scheme', 'Host', 'Port', 'Path']
                writer = csv.DictWriter(file, fieldnames=field_name)
                writer.writerow({'Package': package_name, 'Activity': package_name+activity_name,
                                 'Exported': activity_exported, 'Permission': activity_permission,
                                 'Action': action, 'Category': category,
                                 'MimeType': mimeType, 'Scheme': data_scheme, 'Host': data_host,
                                 'Port': data_port, 'Path': data_path+data_pathPattern+data_pathPrefix})

    return
