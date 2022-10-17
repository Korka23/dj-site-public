{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="{% static 'ksg/css/ksg.css' %}">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/fontawesome.min.css">
    </head>
    <body>
        <aside>
            <img src="{% static 'ksg/img/TFOMS_logo.jpg' %}" alt="Лого">
            <h3>Навигация</h3>
            <ul>
                <a href="{% url 'ksg' %}"><li>КСГ</li></a>
                <a href="{% url 'App_view' %}"><li>App</li></a>
                <a href="{% url 'SP_view' %}"><li>SP</li></a>
                <a href="{% url 'SZP_view' %}"><li>SZP</li></a>
                <a href="{% url 'SZP1_view' %}"><li>SZP1</li></a>
            </ul>
        </aside>
      <main>
            <div style="height:100vh;overflow-y:scroll;">
                <table class="table">
            <thead>
                <tr>
                    <th>Номер МО </th>
                    <th>Название МО</th>

                </tr>
            </thead>
            <tbody>
                <?php
                $dbname='puomp';
                $username='customer_analyst';
                $password='password';
                $host='192.168.0.153';
                $port='5432';
                $option=[];
                $dsn="pgsql:host=".$host.";port=".$port.";dbname=".$dbname;
                $db= new PDO($dsn,$username,$password,$options);
                $stmt = $db -> prepare("select * from public.lic_app_new");
                $stmt -> execute();
                while($row = $stmt -> fetch()){
                ?>
                <tr>
                    <td><?php echo $row['id_prof']?></td>
                    <td><?php echo $row['name']?></td>
                </tr>

            </tbody>
            </table>
            </div>
        </main>
    <script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js"></script>
<!--     <script src="jquery.min.js"></script>--->
    <script src="C:\gits\dj-site\app\templates\app\ddtf.js"></script>
    <script>
        $('#mytable').ddTableFilter();
    </script>
    </body>
</html>