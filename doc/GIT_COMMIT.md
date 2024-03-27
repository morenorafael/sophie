Para cambiar el autor de un commit viejo en Git, puedes seguir estos pasos:

1. Primero, necesitas identificar el hash del commit al que deseas cambiar el autor. Puedes encontrarlo utilizando el comando `git log`, que mostrará el historial de commits en tu repositorio. Por ejemplo:

   ```sh
   git log
   ```

   Esto te mostrará una lista de commits con sus hashes, mensajes y autores.

2. Una vez que hayas identificado el hash del commit al que deseas cambiar el autor, utiliza el siguiente comando:

   ```sh
   git rebase -i <hash_del_commit>^
   ```

   Donde `<hash_del_commit>` es el hash del commit que deseas cambiar y el `^` indica que quieres incluir ese commit en el rebase.

3. Esto abrirá una ventana interactiva o un archivo en tu editor de texto predeterminado, donde verás una lista de commits que van desde el commit que has seleccionado hasta el HEAD de tu rama. Junto al hash de cada commit, verás la palabra "pick". Cambia "pick" por "edit" en el commit al que deseas cambiar el autor y guarda los cambios.

4. Git retrocederá al commit seleccionado y te dirá que estás en "modo de edición".

5. Ahora puedes utilizar el comando `git commit --amend --author="Nombre <correo>"` para cambiar el autor del commit. Reemplaza "Nombre" y "<correo>" con el nombre y el correo electrónico que deseas utilizar.

6. Después de cambiar el autor, utiliza el comando `git rebase --continue` para continuar con el rebase.

7. Si has cambiado más de un commit, tendrás que repetir estos pasos para cada uno.

8. Una vez que hayas terminado de cambiar los autores, utiliza `git push --force` para actualizar el repositorio remoto. Recuerda que `--force` reescribirá la historia del repositorio, así que úsalo con precaución y comunica cualquier cambio en la historia del repositorio a los demás colaboradores.
