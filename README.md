sub_tools  
tools for making subtitles


### bilingual_sub_tool.py
  
  input file format: text file, subtitle language 1 on odd lines, language 2 on even lines
  
  concatenate odd numbered lines with the following line, and add "\n" and style (eg. {\rDefault} in between)
  
  example input:
  
  >这是中文  
  >This is in English  
  >又是中文  
  >English again
  
  output:
  >这是中文\n{\rDefault}This is in English  
  >又是中文\n{\rDefault}English again
  
