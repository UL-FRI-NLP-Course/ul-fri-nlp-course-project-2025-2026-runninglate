from lxml import etree
import pandas as pd
import os

folder = "DGT_2016"

data = []

for file in os.listdir(folder):
    if file.endswith(".tmx"):
        path = os.path.join(folder, file)

        try:
            tree = etree.parse(path)

            for tu in tree.findall(".//tu"):
                texts = {}

                for tuv in tu.findall("tuv"):
                    lang = tuv.attrib.get("lang")
                    text = tuv.findtext("seg")

                    if lang and text:
                        lang = lang.lower()

                        if lang.startswith("en"):
                            texts["en"] = text.strip()
                        elif lang.startswith("sl"):
                            texts["sl"] = text.strip()

                if "en" in texts and "sl" in texts:
                    data.append((texts["en"], texts["sl"]))

        except Exception as e:
            print("Skipped:", file, "Reason:", e)

df = pd.DataFrame(data, columns=["en", "sl"])
df.to_csv("dgt_all.csv", index=False, encoding="utf-8")

print("Total pairs:", len(df))