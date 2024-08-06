namespace Playlist_Shuffle.src.Youtube.UI;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();
        Load += Form1_loader;
    }

    private void Form1_loader(object? sender, EventArgs e)
    {
        // WebBrowser hosts IExplorer, now deprecated
        // Replaced with Edge and WebView2

        WebBrowser browser_form1 = new WebBrowser();
        browser_form1.Dock = DockStyle.Fill;
        browser_form1.Width = this.Width;
        browser_form1.Height = this.Height;
        browser_form1.ScrollBarsEnabled = true;
        browser_form1.Visible = true;
        
        browser_form1.Navigate("https://youtu.be/SB-qEYVdvXA?si=3iVakbcyGV1fHje1");

        this.Controls.Add(browser_form1);
    }
}
