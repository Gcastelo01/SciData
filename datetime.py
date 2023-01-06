def second_parser(time = "00:00:00", separator = ":") -> int:
  """
  @brief: Transforma um horário em seu equivalente em segundos. Pode receber 3 tipos de horários: '00:00:00', '00:00' ou '00'
  
  @param time: String com o horário, em uma das 3 formas possíveis.
  @param separator: Separador dos marcadores de tempo.
  
  @return Inteiro com o valor em segundos do horário especificado
  """
  tList = time.split(separator)
  
  if len(tList) == 3:
    hours = int(tList[0]) * 3600
    minutes = int(tList[1]) * 60
    seconds = int (tList[2])
    
    return hours + minutes + seconds
  
  elif len(tList) == 2:
    minutes = int(tList[0]) * 60
    seconds = int(tList[1]) 
    
    return minutes + seconds
  
  else: return int(tList[0])