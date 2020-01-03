
import csv
from googleapiclient.discovery import build
# my_api_key = "AIzaSyAXdmsIexXhB5LFtdBIXNf7fAaE7YcinPg"
# my_cse_id = "017114304136970662935:0hx9branswe"
my_api_key = "AIzaSyAddtWpFoO_sT7sj_7iwjfHr6B1MVh2wXI"
my_cse_id = "006849828733168866652:8cryghm7x6g"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

queries = []
# queries.append("Đại dương lớn nhất thế giới")
# queries.append("Quốc gia nào nhỏ nhất thế giới về diện tích?")
# queries.append("Thành phố châu Âu nào được gọi là thành phố vĩnh cửu?")
# queries.append("Đảo Korsika(Cooc) thuộc nước nào")
# queries.append("Cảng nào lớn nhất Đông Á?")
# queries.append("Hồ nội địa nào sâu nhất thế giới?")
# queries.append("Đảo St. Helenanằm ở đâu?")
# queries.append("Người ta gọi vùng rừng vành đai Siberi là gì?")
# queries.append("Hãy kể tên 4 nước lớn nhất về diện tích!")
# queries.append("Babylon nằm ở đâu?")
# queries.append("Sông nào dài nhất châu Âu?")
# queries.append("Khi mới thành lập, thành phố NewYork của Mỹ có tên là gì")
# queries.append("Đỉnh núi cao nhất dãy An pơ tên là gì?")
# queries.append("Đỉnh núi cao nhất thế giới tên là gì?")
# queries.append("Tại sao ở nước Anh và một số nước khác xe đi bên trái đường?")
# queries.append("Tại sao coi chim bồ câu là biểu tượng của hoà bình?")
# queries.append("Trà đạo của Nhật Bản đã bắt nguồn và phát triển như thế nào?")
# queries.append("Tại sao phụ nữ Ả RẬP hễ ra ngoài là phải dùng khăn đen che mặt?")
# queries.append("Tại sao ngựa ngủ đứng?")
# queries.append("Tại sao chủng loại thực vật trên núi nhiều hơn so với đồng bằng?")
# queries.append("Vì sao lá trên ngọn rụng cuối cùng?")
# queries.append("tại sao cá bơi ngược dòng?")
# queries.append("Tại sao bầu trời lại có màu xanh?")
# queries.append("Trái đất của chúng ta bao nhiêu tuổi?")
# queries.append("Mặt trời có khi nào ngừng chiếu sáng?")
# queries.append("Nam châm hoạt động như thế nào?")
# queries.append("Tại sao lại có cầu vồng")
# queries.append("Tại sao bọt bong bóng lại có hình cầu?")
# queries.append("Mây được tạo thành từ gì?")
# queries.append("Tại sao nước bốc hơi ở nhiệt độ phòng?")
# queries.append("Mây đen có bao nhiêu nước?")
# queries.append("Có bao nhiêu loài trên Trái đất?")
# queries.append("Thực tế có thật không?")
# queries.append("Sự sống bắt đầu như thế nào?")
# queries.append("Có thể du hành thời gian không?")
# queries.append("Vũ trụ có thực sự vô hạn?")
# queries.append(" Tuổi đời của chúng ta nên đo đếm bằng số năm ta sống hay bằng sự trưởng thành?")
# queries.append("Hà Nội tiếp giáp với bao nhiêu tỉnh?")
# queries.append("Nền công nghiệp nào đứng thứ hai thế giới?")
# queries.append("Trong thế chiến thứ hai, thành phố nào của Nhật Bản bị ném bom nguyên tử?")
# queries.append("Phần mềm nào dùng để nén dữ liệu?")
# queries.append("Phương pháp giảm đau tại chỗ có tên là gì?")
# queries.append("Chim kiwi là loài chim đặc thù của nước nào?")
# queries.append("Quốc kỳ của 11 quốc gia Đông Nam Á có màu gì chung?")
# queries.append("Hà Nội được hình thành từ năm nào?")
queries.append("Châm cứu là phương pháp dùng cây kim đâm vào nơi nào trên cơ thể người?")
queries.append("Quốc gia là gì?")
queries.append("Trong thời kỳ chiếm hữu nô lệ, ở các quốc gia phương Tây, chủ nô gọi nô lệ là gì?")
queries.append("Loài động vật nào lớn nhất trên thế giới?")
queries.append("Thung lũng Silicon là gì?")
queries.append("Đền Ngọc Sơn tọa lạc ở đâu?")
queries.append("EU là gì?")
queries.append("Trùng roi xanh dinh dưỡng bằng cách nào?")
queries.append("13 vạch đỏ trên cờ Mỹ có ý nghĩa gì?")
queries.append("UFO là gì?")
queries.append("Cục dự trữ liên bang Mỹ viết tắt là?")
queries.append("Làng tranh Đông Hồ nay thuộc tỉnh nào nước ta?")
queries.append("Bốn con rồng kinh tế gồm Hàn Quốc, Đài Loan, Hồng Kong và?")
queries.append("Đảng cộng sản Việt Nam được thành lập khi nào?")
queries.append("Vào thời kỳ Phục hưng, ai được coi là vua trộm?")
queries.append("Chòm sao bắc đẩu còn có tên là gì?")
queries.append("Lễ hội Carnaval nổi tiếng là của quốc gia nào?")
queries.append("Hệ thống định vị toàn cầu là gì?")
queries.append("Thiên Chúa và Tin Lành là hai tôn giáo cùng xuất phát từ tôn giáo nào?")
queries.append("Ai là người đầu tiên cho rằng Trái đất quay?")
queries.append("Thành phố nào nằm giữa hai lục địa?")
queries.append("Nước biển là gì?")
queries.append("Đất là gì?")
queries.append("Có bao nhiêu dải ngân hà?")
queries.append("Người châu Á đầu tiên bay vào vũ trụ?")

print("Length of questions: ",len(queries))

with open('science-question-vietnames.csv', mode='a', encoding='utf-8',newline='') as results_file:
    results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for query in queries:
        result = google_search(query, my_api_key, my_cse_id)
        try:
            for item in result['items']:
                results_writer.writerow([item['title'], item['snippet'], query])
        except:
            print("An exception occurred")

