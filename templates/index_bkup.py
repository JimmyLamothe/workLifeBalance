<!DOCTYPE html>
<html>
  <head>
  </head>
  <body style="background-color:#000000";>
    <canvas id="myCanvas" width="780" height="460" style="border:1px solid #000000;">
    </canvas>
    <script src = "{{ url_for('static', filename='initializeCanvas.js') }}"></script>
    <script src = "{{ url_for('static', filename='textProcessing.js') }}"></script>
    <script>displayText("check");</script>
  </body>
</html>
