# A billion Telegram messages about the 2024 US presidential election
* ~1.03B messages, ~43K chats, ~1.5TB decompressed.
* https://app.globus.org/file-manager?origin_id=c3e4dc38-a5e2-47d5-baa2-8b3f5b2a59db&origin_path=%2F (individual .db files, doesn't include chats.db)
* https://doi.org/10.7910/DVN/1M5KHX (chats.db and the entire dataset compressed and split; you need all scraped_part_* files).
* Note that the Globus link will require a subscription (many North American institutions have one). Globus transfers are fast and were tested; they work. The most common problem is not giving write permissions to your desired output directory on the Globus Desktop app (including external storage devices).


Feel free to reach out with any questions!


## Data usage agreement
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0). By using this dataset, you agree to abide by the stipulations in the license and cite the following dataset:

Leonardo Blas, Luca Luceri, and Emilio Ferrara. Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election. 2025. [doi.org/10.7910/DVN/1M5KHX](doi.org/10.7910/DVN/1M5KHX)

And the following manuscript:

Leonardo Blas, Luca Luceri, and Emilio Ferrara. Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election: Development of a Public Dataset. 2024. [doi.org/10.48550/arXiv.2410.23638](doi.org/10.48550/arXiv.2410.23638)

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
