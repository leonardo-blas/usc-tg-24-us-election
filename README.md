# A billion Telegram messages about the 2024 US presidential election

## Releases

### v4 (early March)

### v3 (02-02-25)
* ~1.04B messages, ~43,800 chats, ~1.51TB decompressed.
* https://app.globus.org/file-manager?origin_id=c3e4dc38-a5e2-47d5-baa2-8b3f5b2a59db&origin_path=%2F (individual .db files)
* https://app.globus.org/file-manager?origin_id=021c59ee-d1f7-439a-8907-b0d345ac0441&origin_path=%2F (entire dataset compressed and split).
* Note that the Globus link will require a subscription (many North American institutions have one). Globus transfers are considerably faster and were tested; they work. The most common problem is not giving write permissions to your desired output directory on the Globus Desktop app (including external storage devices).
* Working on more viable distribution methods for this and/or the last dataset version (v4).

### v2 (12-02-24)
* ~630M messages, ~34,000 chats, ~1.1TB decompressed.
* https://academictorrents.com/details/5b3a589175108abbe2afcd8e77c92f97e5b6100f.

### v1 (11-01-24)
* ~490M messages, ~29,900 chats, ~850GB decompressed.
* https://academictorrents.com/details/969ef8cbef89bcd6dc88e85e30a37a630c0ba76f.
* Some files were corrupted and purged---v1 was sanitized---representing a setback of ~50M messages and ~3,000 chats.
  

The collection will continue at least until the end of the year and the dataset will be updated every month.

Feel free to reach out with any questions!


## Data usage agreement
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0). By using this dataset, you agree to abide by the stipulations in the license and cite the following manuscript:

Leonardo Blas, Luca Luceri, and Emilio Ferrara. Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election: Development of a Public Dataset. 2024. https://doi.org/10.48550/arXiv.2410.23638. 

## Instructions
If you you have files like `scraped_part_*`---some distributions may feature one single `scraped.tar.zst`---combine them like:
```
cat scraped_part_* > scraped.tar.zst
```
Once you have `scraped.tar.zst`, decompress like:
```
tar --use-compress-program=unzstd -xvf scraped.tar.zst
```

As mentioned in the paper, some Telegram objects in the SQLite databases were JSON-serialized, UTF-8 encoded, and `zlib` compressed; a version of this dataset in which all `zlib`-compressed entries are decompressed may consume **thrice as much space**. If storage is a concern, it is recommended to decompress and analyze Telegram objects at runtime. If you still wish to decompress a .db file, you can use `decompress.py`.

## Top chats
The N top chats---ranked via unique incoming edge count, an influence proxy metric---can be determined using `chats.db` and `get_top_chats.py`. The default N is 500, but this can be changed within the script.

## Acknowledgements
To all torrent seeders worldwide, thank you for mirroring the dataset! It's greatly appreciated!
<br>
Additionally, we thank AcademicTorrents.com for making our data available worldwide!
