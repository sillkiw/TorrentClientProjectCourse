import bencode as ben,math   #Библиотека для бенкодирования(используется в метафайлах торрента)
from hurry.filesize import size,alternative
from enum import Enum


class Torrent: 
    #Типы файла
    class _Kinds_of_file(Enum):
       SINGLE_FILE,MULTIPLE_FILE = (0,1)
     
    
    def __init__(tr,file_path,name):
        #Путь до торрента
        tr.torrent_path = file_path
        #Имя торрента
        tr.name = name

    #Чтение метаданных с метафайла
    def read_Metafile(tr):
        #Открытие торрент-файла
        with open(tr.torrent_path,"rb") as torrent_file:
            #Чтение файла и декодирование бенкодинга
            tr.metainfo = ben.bdecode(torrent_file.read())
            #url-адресс трекера
            tr.announce = tr.metainfo['announce']
            #info - информация о файлах торрента, частях и их размеров
            tr.info = tr.metainfo['info']
            #piece length - размер одной части
            tr.piece_length = tr.info['piece length']
            #pieces - части файлов / файла
            tr.pieces = tr.info['pieces']
            if 'files' in tr.metainfo['info']:
                #Имя главной папки
                tr.name = tr.info['name']
                tr.files = tr.info['files']
                #Тип файловой системы
                tr.kind_file = Torrent._Kinds_of_file.MULTIPLE_FILE
                #Общий размер
                tr.length = 0
                for file in tr.files:
                    tr.length += file['length']
            else:
                #Имя единственного файла
                tr.name = tr.info['name']
                #Тип файловой системы
                tr.kind_file = Torrent._Kinds_of_file.SINGLE_FILE
                #Размер файла
                tr.length = tr.info['length']
            tr.number_of_pieces = math.cell(tr.length/tr.piece_length)
            #Представление размера файлов в красивом виде    
            tr.size =  size(tr.length,system=alternative)
  
    
                    
           