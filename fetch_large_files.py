"""補抓 jailbreak_benchmarks 裡因為超過 GitHub 100MB 上限而沒有放進這個 repo 的大檔。

WildJailbreak 需要先在 https://huggingface.co/datasets/allenai/wildjailbreak 同意 AI2 授權，
並用 `hf auth login` 登入，否則會回 403。

用法：python fetch_large_files.py
"""
import io, urllib.request, zipfile

from huggingface_hub import snapshot_download

snapshot_download("allenai/wildjailbreak", repo_type="dataset", local_dir="WildJailbreak",
                  allow_patterns=["train/train.tsv"])
print("OK WildJailbreak/train/train.tsv")

# DAN 的 forbidden_question_set_with_prompts.csv 在來源 repo 裡是 zip
url = ("https://github.com/verazuo/jailbreak_llms/raw/main/data/"
       "forbidden_question/forbidden_question_set_with_prompts.csv.zip")
with urllib.request.urlopen(url) as r:
    zipfile.ZipFile(io.BytesIO(r.read())).extract("forbidden_question_set_with_prompts.csv",
                                                  "DAN/forbidden_question")
print("OK DAN/forbidden_question/forbidden_question_set_with_prompts.csv")
