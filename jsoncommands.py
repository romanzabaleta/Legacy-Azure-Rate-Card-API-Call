import json
import subprocess


class jsoncmd():
    def json(self):
        output = str(subprocess.check_output(self, stderr=subprocess.STDOUT, shell=True))
        output = output[output.find("{"):]
        output = output[:output.rfind("}") + 1]
        output = output.replace("\\r\\n", "")
        output = output.replace(" ", "")
        output = output.replace(",", ", ")
        return output

    def tojson(self):
        output = jsoncmd.json(self)
        output = json.loads(output)
        return output

    def savejson(self, filename):
        output = jsoncmd.tojson(self)
        with open(filename + '.json', 'w') as outfile:
            outfile.write(json.dumps(output))
            outfile.close()
        print(filename + ".json created/updated")
        return output

    def loadjson(self):
        f = open(self, 'r')
        output = json.load(f)
        return output