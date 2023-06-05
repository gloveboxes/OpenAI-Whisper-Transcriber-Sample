using CommunityToolkit.Maui.Storage;
using Newtonsoft.Json.Linq;

namespace WhisperNamespace;



public partial class AudioPage : ContentPage
{
    private List<string> _audioFiles = new List<string>();

    public AudioPage()
    {
        InitializeComponent();
    }


    public IEnumerable<string> FilterFiles(string path, params string[] exts)
    {
        return
            exts.Select(x => "*." + x) // turn into globs
            .SelectMany(x =>
                Directory.EnumerateFiles(path, x)
                );
    }

    private async void BrowseButton_Clicked(object sender, EventArgs e)
    {
        CancellationTokenSource source = new();
        CancellationToken token = source.Token;
        var result = await FolderPicker.Default.PickAsync(token);

        if (result.IsSuccessful)
        {
            var r = result.Folder.Path; // SaveLocation is a textbox in my XAML file
            if (r != null)
            {
                // Clear the existing audio files and dropdown list items
                _audioFiles.Clear();
                AudioDropdown.Items.Clear();

                var audioFiles = FilterFiles(r, "mp3", "wav", "m4a");
                _audioFiles.AddRange(audioFiles);

                // Populate the dropdown list with the audio file names
                foreach (var audioFile in audioFiles)
                {
                    var fileName = Path.GetFileName(audioFile);
                    AudioDropdown.Items.Add(fileName);
                }
            }
        }
    }

    private async void UploadButton_Clicked(object sender, EventArgs e)
    {
        // Get the selected audio file path from the dropdown list
        var selectedAudioFile = _audioFiles[AudioDropdown.SelectedIndex];
        ResponseLabel.Text = "Transcribing";

        // Post the file to the web server using HttpClient
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("api-key", WhisperKey.Text); // Add the API key to the header

        var fileContent = new ByteArrayContent(File.ReadAllBytes(selectedAudioFile));
        var response = await httpClient.PostAsync(String.Format("{0}/transcribe", WhisperEndpoint.Text), fileContent);

        if (response.IsSuccessStatusCode)
        {
            var responseContent = await response.Content.ReadAsStringAsync();
            var jsonObject = JObject.Parse(responseContent);
            ResponseLabel.Text = (string)jsonObject["transcription"];
        }
        else
        {
            ResponseLabel.Text = "Failed. Check endpoint and endpoint key";
        }
    }
}