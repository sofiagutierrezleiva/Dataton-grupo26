# Dataton-grupo26

### Librerías necesarias para ejecutar el código:
* TensorFlow versión: 2.16.1
* Pillow (PIL) versión: 9.5.0
* NumPy versión: 1.26.2
* OpenCV versión: 4.9.0
* SciKit-Learn versión: 1.4.0
* Matplotlib versión: 3.7.1
* Albumentations versión: 1.4.3
* Seaborn versión: 0.13.2
* Segment_anything (SAM): 1.0

### Cómo correr el código (antes)
1. Para bajar las imágenes dese dataCube se debe ejecutar ```get_data.ipynb```
  En este archivo se recorren los satelites seleccionados (landsat's 5, 8 y 9) y, utilizando el código base del ue disponiamos, seleccionamos las imagenes con menor ruido (nubes principalmente) y guardamos la imagen en RGB y en escala de rojos (para desarrollar las máscaras posteriormente). Se debe considerar también que se toman diferentes tiempos para cada satélite para aumentar la cantidad de datos y la disposición del glaciar.
 
2. Con la ayuda de ```img_corrector.py``` se pueden generar máscaras con tan solo los colores blancos y negros, lo cual facilitó el desarrollo de los resultados requeridos.
  
3. Las imaáenes RGB obtenidas de la descarga de archivos desde la nube y su post delineamiento semántico manual para entrenamiento, se guardan en ```data/originals/imgs``` y ```data/originals/masks```, respectivmente. Adicionalmente y a modo de prueba se registraron también las imagenes correspondientes solo a la banda R en ```data/originals/imgs_Red```.

  El post procesamiento de estos datos se realiza en ```augmentation.ipynb``` cuyo objetivo es aumentar el set de entrenamiento a partir de modificaciones a las imagenes originales. Se presentan 2 acercamientos para esta tarea:
    a. En primer lugar, con la celda *Aumento de dataset a partir de seccionar las imágenes* se seleccionan los pixeles que se desea tengan los lados de cada segmentación (NEW_SIZE) y cada cuántos inicia una nueva segmentación (DEPHASE). Una vez que se corre el codigo, todas las imagenes generadas se guardan en ```data/augmentated/aug_imgs``` y ```data/augmentated/aug_masks```.
    b. En segundo, y no excluyente con el anterior (mas requeriría cierto ajuste de código en los paths para ejecutarlos en conjunto) se pueden realizar diversas modificaciones geométricas como trasponer, reflejar vertical y horizontalmente, etc. De igual forma al caso anterior las imagenes se guardan en ```data/augmentated/aug_imgs``` y ```data/augmentated/aug_masks```. 
    
4. Una vez que se ha obtenido el set de datos, simplemente se deben correr secuencialemnte todas las celdas de ```unet.ipynb```, donde se entrenará el modelo y pueden observarse algunos resultados como la accuracy para cada clase (glaciar, no-glaciar) y los gráficos de evolución por época de los parámetros de loss.

### Cómo correr el código (actual) 
El modelo no funcinó como esperabamos por varias razones, pero destaca la falta de material de entrenamiento y lo especifico del entrenamiento, esto es que se trabajó unica y exclusivamente con el mismo glaciar el cual, pese al paso del tiempo no varía significativamente su forma.

Ante esta situación, y dado que encontramos SAM, un modelo de segmentación de imágenes desarrollado por META, optamos por implementar dicho modelo en nuestro área de enfoque, entrenándola con nuestros datos (lo cual realmente no afectó tanto dado que tenía un trasfondo de billones de imagenes a lo que le agregamos aproximadamente 10.000 mas), y centrarnos en el análisis de superficie. Esto se traduce en que obtenemos la segmentación del glaciar y utilizando una escala según cuantos metros representa cada pixel, obtenemos la superficie del glaciar en la imagen seleccionada. Ideamos un método para seleccionar la máscara correcta para cada imágen pero no tuvimos tiempo para implementarlo.

Para correr el código basta con correr el archivo main.ipynb que se ecnuentra en la carpeta ```model_env```, aquí debemos anotar la escala de la imágen (metros/pixel) y cambiar el path de la imagen analizada.
  
### Links de bibliografía:
* https://www.nature.com/articles/s41467-021-26578-0
* https://tc.copernicus.org/articles/14/565/2020/
* https://www.cambridge.org/core/journals/journal-of-glaciology/article/deep-learning-speeds-up-ice-flow-modelling-by-several-orders-of-magnitude/748E962A103D2AF45F4CA8823C88C0C0
* https://www.frontiersin.org/articles/10.3389/frsen.2023.1161530/full#B2
* https://www.scielo.org.mx/scielo.php?pid=S2663-39812022000100133&script=sci_abstract&tlng=es
* https://www.revistaterraaustralis.cl/index.php/rgch/article/download/129/69/1525
* https://revistas.uchile.cl/index.php/IG/article/download/41215/44541/0
* https://dialnet.unirioja.es/servlet/articulo?codigo=927052



