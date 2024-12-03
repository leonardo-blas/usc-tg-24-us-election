# A billion Telegram messages about the 2024 US presidential election

## Releases

### v2 (12-02-24)
* ~630M messages, ~34,000 chats, ~1.1TB.
* https://academictorrents.com/details/5b3a589175108abbe2afcd8e77c92f97e5b6100f.
* Lower message yield than expected due to prioritizing updating over discovering chats. v3 should (hopefully) have a higher yield. Additionally, we are considering scraping until the end of January or February to capture messages about the presidential transition. 

### v1 (11-01-24)
* ~490M messages, ~29,900 chats, ~850GB.
* https://academictorrents.com/details/969ef8cbef89bcd6dc88e85e30a37a630c0ba76f.
* https://drive.google.com/drive/folders/1cC5vDqe9_vQjODJ5FDikAPOhjn2MI4HQ?usp=drive_link.
* Some files were corrupted and purged---v1 was sanitized---representing a setback of ~50M messages and ~3,000 chats.
  

The collection will continue at least until the end of the year and the dataset will be updated every month.


## Data usage agreement
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0). By using this dataset, you agree to abide by the stipulations in the license and cite the following manuscript:

Leonardo Blas, Luca Luceri, and Emilio Ferrara. Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election: Development of a Public Dataset. 2024. https://doi.org/10.48550/arXiv.2410.23638. 

## Instructions
Combine the split files like:
```
cat scraped_part_* > scraped.tar.zst
```
And decompress like:
```
tar --use-compress-program=unzstd -xvf scraped.tar.zst
```

The decompressed `scraped` folder weights around 850GB. Furthermore, as mentioned in the paper, some Telegram objects in the SQLite databases were JSON-serialized, UTF-8 encoded, and `zlib` compressed; a version of this dataset in which all `zlib`-compressed entries are decompressed may consume **thrice as much space**. If storage is a concern, it is recommended to decompress and analyze Telegram objects at runtime. If you still wish to decompress a .db file, you can use `decompress.py`.

## Top chats
The N top chats---ranked via unique incoming edge count, an influence proxy metric---can be determined using `chats.db` and `get_top_chats.py`. The default N is 500, but this can be changed within the script.

## Acknowledgements
To all torrent seeders worldwide, thank you for mirroring the dataset! It's greatly appreciated!
