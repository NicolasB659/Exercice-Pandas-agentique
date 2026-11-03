import pandas as pd

DATA = "data/"

train = pd.read_csv(DATA + "HYE_train.tsv", sep="\t")
test_in = pd.read_csv(DATA + "HYE_test_in_domain.tsv", sep="\t")
test_out = pd.read_csv(DATA + "HYE_test_out_domain.tsv", sep="\t")
tagset_df = pd.read_csv(DATA + "HYE_tagset.txt", sep="\t", header=None, engine="python")

# ---------- Q1 ----------
print("Q1")
print("5 categories (pos) les plus frequentes dans HYE_train.tsv :")
print(train["pos"].value_counts().head(5).to_string())
print()

# ---------- Q2 ----------
print("Q2")
compose = train["pos"].str.contains("@")
print("Proportion de formes composees (@ dans pos) :", round(compose.mean(), 4))
print("5 combinaisons les plus frequentes :")
print(train.loc[compose, "pos"].value_counts().head(5).to_string())
print()

# ---------- Q3 ----------
print("Q3")
art = train["pos"].str.endswith("@PRO+Dem").sum()
prep = train["lemma"].str.startswith("զ@").sum()
print("Mots du train dont le pos finit par @PRO+Dem (article suffixe) :", art)
print("Mots du train dont le lemma commence par զ@ (preposition զ) :", prep)
print()

# ---------- Q4 ----------
print("Q4")
tagset = tagset_df[0].str.strip().unique()  # strip : certains noms ont une espace finale
lab = train[["pos"]].drop_duplicates()       # une ligne par etiquette
lab["part"] = lab["pos"].str.split("@")      # liste des parties
parts = lab.explode("part")                  # une partie par ligne, alignee avec pos
invalid_part = ~parts["part"].isin(tagset)   # partie absente du tagset
bad_labels = parts.loc[invalid_part, "pos"].unique()  # etiquettes dont une partie est invalide
bad_mask = train["pos"].isin(bad_labels)
print("Etiquettes du train absentes du tagset, avec leur effectif :")
print(train.loc[bad_mask, "pos"].value_counts().to_string())
print("Total d'occurrences de ces etiquettes :", int(bad_mask.sum()))
print()

# ---------- Q5 ----------
print("Q5")
dico = train[["form", "pos"]].drop_duplicates("form").rename(columns={"pos": "pos_dico"})

merged_in = test_in.merge(dico, on="form", how="left")
score_in = (merged_in["pos"] == merged_in["pos_dico"]).mean()

merged_out = test_out.merge(dico, on="form", how="left")
score_out = (merged_out["pos"] == merged_out["pos_dico"]).mean()

print("Score sur HYE_test_in_domain.tsv :", round(score_in, 4))
print("Score sur HYE_test_out_domain.tsv :", round(score_out, 4))
print("Baisse in-domain -> out-domain :", round(score_in - score_out, 4))
print("En grec la baisse etait de 0,73 - 0,51 = 0,22.")
