# A billion Telegram messages about the 2024 US presidential election
The dataset is available at: https://academictorrents.com/details/969ef8cbef89bcd6dc88e85e30a37a630c0ba76f

To combine the split files, do:
```
cat scraped_part_* > scraped.tar.zst
```
And decompress like:
```
tar --use-compress-program=unzstd -xvf scraped.tar.zst
```

The decompressed `scraped` folder weights around 850GB. Furthermore, as mentioned in the paper, some Telegram objects in the SQLite databases were JSON-serialized, UTF-8 encoded, and `zlib` compressed. A version of this dataset in which all `zlib` compressed entries are decompressed may consume around 2.6TB. If storage is a concern, it is recommended to decompress and analyze Telegram objects at runtime. Additionaly, if you don't need the timestamps, it is recommended to drop those columns, as it will save a considerable amount of space.

Note: Our torrent seeders are currently overwhelmed. We are looking into providing better availability. Apologies for the slow download rates.


## Data usage agreement
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0). By using this dataset, you agree to abide by the stipulations in the license and cite the following manuscript:

Leonardo Blas, Luca Luceri, and Emilio Ferrara. Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election: Development of a Public Dataset. 2024. arXiv, https://arxiv.org/abs/2410.23638.

