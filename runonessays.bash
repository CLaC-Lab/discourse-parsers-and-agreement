for file in ICNALE/*.txt
do
  if [ ! -s ${file}.json ]
  then
    rst_parse -g segmentation_model.C0.5 -p rst_parsing_model.C0.5 "$file" >> ${file}.json
  else
    echo ${file}.json + "File already parsed"
  fi
done

