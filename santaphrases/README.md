In order to create custom song + phrase mp3's for santa to play, simply record your phrases as mp3 files. I use audacity and a laptop to do this.
Download the music and santa_MkStockPhrases.py directory and script. Create an empty santaphrases and mixedphrases directory.
Drop your phrases into the santaphrases directory and run the santa_MkStockPhrases.py script. 
  If it doesn't run, you're probably missing pydub library.  Run this command - pip install pydub
You'll have mixed mp3's (music + phrases) show up in the mixedphrases directory.
Remove the old mp3's from your pico and copy these in instead. Now when you click the button, your santa will play the new mp3's!
