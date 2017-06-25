<?php

$curl = curl_init();
curl_setopt_array(
    $curl, [
        CURLOPT_URL            => 'http://www.magicreadalong.com/episode?format=rss',
        CURLOPT_USERAGENT => 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
        CURLOPT_RETURNTRANSFER => 1
    ]
);

$output = curl_exec($curl);

if (!$output) {
    print curl_error($curl);
}

curl_close($curl);

$xml = simplexml_load_string($output);
$xml = json_encode($xml);
$xml = json_decode($xml);

$download = function ($url) {
    $name = explode('/', $url);
    $name = end($name);
    $mp3 = file_get_contents($url);
    if(!file_exists($name) && file_put_contents($name, $mp3, FILE_APPEND)) {
        print "downloaded" . $name . "\n";
    } else {
        print $name . " was NOT downloaded" . "\n";
    }
};

foreach ($xml->channel->item as $pub) {
    $url = reset($pub->enclosure)->url;
    $download($url);
}
