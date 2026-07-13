# YaSara v4.18.1 Stable CLI Rescue

Extract into:

```text
D:\yasara_clean
```

Run:

```cmd
cd /d D:\yasara_clean
python scripts\repair_yasara_cli_v4_18_1.py
python yasara.py patch
python yasara.py test
python yasara.py start
```

This repairs the broken `from __future__` issue and replaces `yasara.py` with a stable long-term CLI.
