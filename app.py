<!DOCTYPE html>
<html>
<head>
    <title>Identification Result</title>
</head>
<body>
    <h1>Victim Identified!</h1>

    <p><strong>Image:</strong> {{ result.image }}</p>
    <p><strong>Mandible Angle:</strong> {{ result.mandible_angle }}</p>
    <p><strong>Third Molar:</strong> {{ result.third_molar }}</p>
    <p><strong>Fillings:</strong> {{ result.fillings }}</p>
    <p><strong>Matching Score:</strong> {{ result.score }}%</p>

    <br>
    <a href="/identify">Identify Another</a>
    <br>
    <a href="/">Back to Home</a>
</body>
</html>
