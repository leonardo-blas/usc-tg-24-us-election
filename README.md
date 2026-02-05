# A billion Telegram messages about the 2024 US presidential election
* ~1.03B messages, ~43K chats, ~0.8TB (distilled).
* https://huggingface.co/datasets/leonardoblas/us_election_2024_telegram_distilled.
* The raw version is no longer available. The distilled version flattens the raw JSON documents nicely into a SQL format. Some fields were dropped, but the most important ones were retained.


Feel free to reach out with any questions!


## Data usage agreement
This dataset is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. For more information, refer to [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/). By using this dataset, you agree to abide by the stipulations in the license and cite the following manuscript:

```tex
@inproceedings{10.1145/3701716.3715297,
  author = {Blas, Leonardo and Luceri, Luca and Ferrara, Emilio},
  title = {Unearthing a Billion Telegram Posts about the 2024 U.S. Presidential Election: Development of a Public Dataset},
  year = {2025},
  isbn = {9798400713316},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://doi.org/10.1145/3701716.3715297},
  doi = {10.1145/3701716.3715297},
  abstract = {With its lenient moderation and long-standing associations with potentially unlawful activities, Telegram has become an incubator for problematic content, frequently featuring conspiratorial, hyper-partisan, and fringe narratives. Exacerbating these concerns, investigations have underscored Telegram's role in organizing violent acts, such as those that occurred during the Capitol Hill attack on January 6, 2021. As of 2024, Telegram represents a focal arena for societal and political discourse, warranting close attention from the research community, regulators, and the media. Thus, we present a Telegram dataset focused on the 2024 US Presidential Election, comprising over 43 thousand chats and over 1 billion messages, and featuring chats' details, profile pictures, messages, and user information. In addition, we present application scenarios for this dataset, such as the construction of a network of chats, which can facilitate the analysis of interconnected communities, and a sample of harmful messages aimed at mobilizing supporters ahead of now-reported protests, which can serve as a case study to explore coordinated dynamics from the online to the offline world. This resource represents the largest public Telegram dataset to date, offering an unprecedented opportunity to study political discussion on Telegram.},
  booktitle = {Companion Proceedings of the ACM on Web Conference 2025},
  pages = {729–732},
  numpages = {4},
  keywords = {dataset, elections, keywords{telegram, politics}},
  location = {Sydney NSW, Australia},
  series = {WWW '25}
}
```


If you wish to use or know how we assigned the "political" labels, please cite/refer to:
```tex
@article{Blas2025Telegram,
  author  = {Blas, Leonardo and Saraf, Diya and Salkar, Tanishq and Adadurova, Nora and Luceri, Luca and Ferrara, Emilio},
  title   = {Large-scale detection of multilingual coordinated activity on Telegram},
  journal = {npj Complexity},
  year    = {2025},
  volume  = {2},
  pages   = {33},
  month   = nov,
  doi     = {10.1038/s44260-025-00056-w},
  url     = {https://doi.org/10.1038/s44260-025-00056-w},
  publisher = {Springer Nature}
}
```


## Top chats
The N top chats---ranked via unique incoming edge count, an influence proxy metric---can be determined using `chats.db` and `get_top_chats.py`. The default N is 500, but this can be changed within the script.
