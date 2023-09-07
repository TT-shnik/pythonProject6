ReadMe
Чтобы запустить программу следует выполнить следующие действия:

1. Скачать файл( можно скачать полностью архив) auto-test-megaputer.exe
2. После загрузки файла в формате zip разархивируйте его
3. Запустите файл auto-test-megaputer.exe

Если нет действующего WebDriver'а:
Чтобы все работало нужно установить WebDriver( в частности для браузера Microsoft Edge):
Убедитесь, что установленная вами версия Microsoft Edge WebDriver соответствует версии вашего браузера
 1. Зайдите в браузер Microsoft Edge, перейдите по адресу Edge://settings/help и запишите свою версию Microsoft Edge
 2. Перейдите в Microsoft Edge WebDriver. https://developer.microsoft.com/microsoft-edge/tools/webdriver/
 3. В разделе «Получить последнюю версию» страницы выберите платформу в канале, которая соответствует номеру вашей версии Microsoft Edge:
 4. После завершения загрузки извлеките исполняемый файл msedgedriver в удобное для вас место.  Добавьте папку, в которой находится исполняемый файл, в переменную среды PATH.

Как добавить папку, в которой находится исполняемый файл ( msedgedriver.exe), в переменные среды PATH:
После разархивирования архива с WebDriver’ом браузера Microsoft Edge скопируйте путь, по которому сохранен файл Edge WebDriver, чтобы установить свойства системы в переменных среды.  Выполните следующие действия, чтобы установить путь в переменных среды:
1. Щелкните правой кнопкой мыши «Мой компьютер» и выберите «Свойства».
2. Нажмите «Изменить настройки», а затем перейдите на вкладку «Дополнительно».
3. Теперь выберите переменные среды на вкладке «Дополнительно».
4. Теперь из доступных параметров в разделе «Системные переменные» выберите параметр «Путь» и нажмите «Изменить». 
5. В конце строки введите точку с запятой «;» и вставьте путь.  вашего файла Edge WebDriver, который вы скопировали ранее, и нажмите «ОК».