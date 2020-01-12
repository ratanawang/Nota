from google.cloud import language_v1
from google.cloud.language_v1 import enums
import re

notes = ""  # the string saved to the text file, used by front end


def sample_analyze_entities(text_content):
    text_content = re.split('[?.!]', text_content)
    text_content.pop(len(text_content)-1)

    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"

    with open("notes.txt", "w") as file:
        file.write(str(notes))

    for text in text_content:

        with open("notes.txt", "a") as file:
            file.write("---------------\n")

        document = {"content": text, "type": type_, "language": language}

        encoding_type = enums.EncodingType.UTF8

        response = client.analyze_entities(document, encoding_type=encoding_type)
        for entity in response.entities:
            print("")
            print(u"Representative name for the entity: {}".format(entity.name))
            print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
            if enums.Entity.Type(entity.type).name == "DATE":
                with open("notes.txt", "a") as file:
                    file.write("{}\n".format(entity.name))
            print(u"Salience score: {}".format(entity.salience))
            for metadata_name, metadata_value in entity.metadata.items():
                print(u"{}: {}".format(metadata_name, metadata_value))

            for mention in entity.mentions:
                print(u"Mention text: {}".format(mention.text.content))
                print(
                    u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
                )

        print(u"Language of the text: {}".format(response.language))

        temp = {}
        for entity in response.entities:
            temp[entity.mentions[0].text.content] = entity.salience
        print()
        print("Analysis begins below.....")
        while True:
            if len(temp) > 0:
                ent = max(temp.values())
                for key in temp.keys():
                    if temp[key] == ent:
                        print("{}:".format(key))
                        print("---has a salience score of: {}".format(ent))
                        if ent > 0:
                            with open("notes.txt", "a") as file:
                                file.write("{}\n".format(key))
                        del temp[key]
                        break
            else:
                break


sample_analyze_entities(u"{}".format(input("Enter entities text: ")))
