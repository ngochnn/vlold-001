https://gist.github.com/ASC689561/7ede0d6a8b8676d553d6be4bcf95b645
lấu bài C ra xong quăng lên Git
triệu huy nói vạy
C++ á

Thuc Nguyen
lan anh có thể chụp dùm t mấy cái code trong trang đó ko bà

Gái Chưa Chồng
lấy html luôn k bà
:)))

Thuc Nguyen
lấy luôn bà

Hân
<!DOCTYPE html>
<html>
    <head>
        <title>Giải phương trình bậc hai</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <?php 
            $result = '';
            if (isset($_POST['calculate']))
            {
            }
        ?>
        <h1>Giải phương trình bậc hai</h1>
        <form method="post" action="">
            <input type="text" style="width: 20px" name="a" value=""/>x <sup>2</sup>
            +
            <input type="text" style="width: 20px" name="b" value=""/>x
            + 
            <input type="text" style="width: 20px" name="c" value=""/>
            = 0
            <br/><br/>
            <input type="submit" name="calculate" value="Tính" />
        </form>
        <?php echo $result; ?>
    </body>
</html>
