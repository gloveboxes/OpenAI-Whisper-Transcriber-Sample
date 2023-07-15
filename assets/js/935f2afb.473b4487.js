"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[53],{1109:e=>{e.exports=JSON.parse('{"pluginId":"default","version":"current","label":"Next","banner":null,"badge":false,"noIndex":false,"className":"docs-version-current","isLast":true,"docsSidebars":{"tutorialSidebar":[{"type":"link","label":"Introduction","href":"/OpenAI-Whisper-Transcriber-Sample/","docId":"Introduction"},{"type":"link","label":"Intro to OpenAI Functions","href":"/OpenAI-Whisper-Transcriber-Sample/OpenAI-Functions","docId":"OpenAI-Functions"},{"type":"link","label":"Start the Home Assistant","href":"/OpenAI-Whisper-Transcriber-Sample/Assistant","docId":"Assistant"},{"type":"category","label":"Create a Whisper Endpoint","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Whisper server setup","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Server/Whisper-Server-Setup","docId":"Whisper-Server/Whisper-Server-Setup"},{"type":"link","label":"Windows with an NVidia GPU","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Server/Whisper-Server-WSL","docId":"Whisper-Server/Whisper-Server-WSL"},{"type":"link","label":"Ubuntu with an NVidia GPU","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Server/Whisper-Server-Ubuntu","docId":"Whisper-Server/Whisper-Server-Ubuntu"},{"type":"link","label":"Systems without an NVidia GPU","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Server/Whisper-Server-no-GPU","docId":"Whisper-Server/Whisper-Server-no-GPU"}],"href":"/OpenAI-Whisper-Transcriber-Sample/category/create-a-whisper-endpoint"},{"type":"category","label":"Transcribe with Whisper","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Whisper Client Setup","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Client/Whisper-Client-Setup","docId":"Whisper-Client/Whisper-Client-Setup"},{"type":"link","label":"The Whisper GUI app","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Client/Whisper-GUI-App","docId":"Whisper-Client/Whisper-GUI-App"},{"type":"link","label":"The Whisper Web App","href":"/OpenAI-Whisper-Transcriber-Sample/Whisper-Client/Whisper-Web-App","docId":"Whisper-Client/Whisper-Web-App"}],"href":"/OpenAI-Whisper-Transcriber-Sample/category/transcribe-with-whisper"},{"type":"category","label":"Proxies","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Whisper Intranet Access","href":"/OpenAI-Whisper-Transcriber-Sample/Proxies/Whisper-intranet","docId":"Proxies/Whisper-intranet"},{"type":"link","label":"Whisper Anywhere Access","href":"/OpenAI-Whisper-Transcriber-Sample/Proxies/Whisper-ngrok","docId":"Proxies/Whisper-ngrok"}]},{"type":"category","label":"Testing","collapsible":true,"collapsed":true,"items":[{"type":"link","label":"Testing with Postman","href":"/OpenAI-Whisper-Transcriber-Sample/Testing/Whisper-Postman","docId":"Testing/Whisper-Postman"}]},{"type":"link","label":"Finished","href":"/OpenAI-Whisper-Transcriber-Sample/Summary","docId":"Summary"},{"type":"link","label":"References","href":"/OpenAI-Whisper-Transcriber-Sample/References","docId":"References"}]},"docs":{"Assistant":{"id":"Assistant","title":"Start the Home Assistant","description":"Platform support","sidebar":"tutorialSidebar"},"Introduction":{"id":"Introduction","title":"Introduction","description":"<Social","sidebar":"tutorialSidebar"},"OpenAI-Functions":{"id":"OpenAI-Functions","title":"Intro to OpenAI Functions","description":"This sample uses OpenAI Functions extensive to power the home assistant. OpenAI Functions enables you to describe functions to gpt-3.5-turbo-0613 and gpt-4-0613 models and later, and have the GPT model intelligently select which function (if any) best matches the data in the prompt. The function definitions along with the prompt are passed to the OpenAI Chat Completion API. The GPT model then determines which function best matches the prompt and populates a JSON object using the function JSON schema and prompt data. If there is a successful match, the chat completion API returns the function name and the JSON object/entity.","sidebar":"tutorialSidebar"},"Proxies/Whisper-intranet":{"id":"Proxies/Whisper-intranet","title":"Whisper Intranet Access","description":"If you are running the Whisper Server in WSL and want to run the Whisper GUI app from a different computer on the same LAN, then run the proxy.py app on the same machine as the Whisper Transcriber Service. This is because the Whisper Transcriber Service REST API is not accessible from outside the Windows WSL environment. The proxy app runs on Windows and will forward the REST API calls to the Whisper Transcriber Service running in WSL.","sidebar":"tutorialSidebar"},"Proxies/Whisper-ngrok":{"id":"Proxies/Whisper-ngrok","title":"Whisper Anywhere Access","description":"If you want to access the Whisper Server running in WSL or Desktop Linux from a different computer or over the internet then you can use ngrok.","sidebar":"tutorialSidebar"},"References":{"id":"References","title":"References","description":"1. FastAPI","sidebar":"tutorialSidebar"},"Summary":{"id":"Summary","title":"Finished","description":"Congratulations! You have successfully installed and run the Home Assistant and Whisper Transcriber Samples \ud83c\udf89","sidebar":"tutorialSidebar"},"Testing/Whisper-Postman":{"id":"Testing/Whisper-Postman","title":"Testing with Postman","description":"The easiest way to test the Whisper Transcriber Service is with Postman.","sidebar":"tutorialSidebar"},"Whisper-Client/Whisper-Client-Setup":{"id":"Whisper-Client/Whisper-Client-Setup","title":"Whisper Client Setup","description":"This sample also includes a client app that can be used to interact with the Whisper Transcriber Service.  The client app can be used to:","sidebar":"tutorialSidebar"},"Whisper-Client/Whisper-GUI-App":{"id":"Whisper-Client/Whisper-GUI-App","title":"The Whisper GUI app","description":"Using Whisper GUI app, you can transcribe pre-recorded audio files and audio recorded from your microphone.","sidebar":"tutorialSidebar"},"Whisper-Client/Whisper-Web-App":{"id":"Whisper-Client/Whisper-Web-App","title":"The Whisper Web App","description":"On the same computer as the Whisper Transcriber Service, you can run the Whisper Transcriber web app. The web app is a simple web page that allows you to select an audio file and transcribe it using the Whisper Transcriber Service.","sidebar":"tutorialSidebar"},"Whisper-Server/Whisper-Server-no-GPU":{"id":"Whisper-Server/Whisper-Server-no-GPU","title":"Systems without an NVidia GPU","description":"The Whisper Transcriber Service runs on Windows, macOS, and Linux systems without an NVidia GPU, it\'ll just run slower as the Whisper model run on the CPU.","sidebar":"tutorialSidebar"},"Whisper-Server/Whisper-Server-Setup":{"id":"Whisper-Server/Whisper-Server-Setup","title":"Whisper server setup","description":"The ideal and most performant configuration for running the OpenAI Whisper sample is with Windows with WSL 2 and an NVidia GPU or a Linux desktop system with an NVidia GPU.","sidebar":"tutorialSidebar"},"Whisper-Server/Whisper-Server-Ubuntu":{"id":"Whisper-Server/Whisper-Server-Ubuntu","title":"Ubuntu with an NVidia GPU","description":"The recommended configuration for running the OpenAI Whisper sample on Ubuntu is:","sidebar":"tutorialSidebar"},"Whisper-Server/Whisper-Server-WSL":{"id":"Whisper-Server/Whisper-Server-WSL","title":"Windows with an NVidia GPU","description":"The recommended configuration for running the OpenAI Whisper sample on Windows is with WSL 2 and an NVidia GPU. This configuration is popular and provides the best performance. The OpenAI Whisper speech to text transcription runs consistently faster on WSL 2 than natively on Windows.","sidebar":"tutorialSidebar"}}}')}}]);