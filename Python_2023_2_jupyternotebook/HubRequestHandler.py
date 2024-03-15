from http.server import SimpleHTTPRequestHandler
import time
from urllib import parse

class HubRequestHandler(SimpleHTTPRequestHandler): # SimpleHTTPRequestHandler를 상속받아 HubRequestHandler 클래스를 구현

    def do_GET(self):
        print(self.path)
        result = parse.urlsplit(self.path)
        if self.path == '/': self.writeHome() # 홈
        elif self.path == '/meas_one_volt': self.writeMeasOneVolt()
        elif result.path == '/sample_volt': self.writeSampleVolt(result.query)
        elif self.path == '/meas_one_light': self.writeMeasOneLight()
        elif result.path == '/sample_light': self.writeSampleLight(result.query)
        elif result.path == '/servo_move_0': self.writeServoMove(0)
        elif result.path == '/servo_move_90': self.writeServoMove(90)
        elif result.path == '/servo_move_180': self.writeServoMove(180)
        elif result.path == '/servo_move': self.writeServoMoveQs(result.query)
        elif result.path == '/led': self.writeLedColor(result.query)
        elif result.path == '/buzzer': self.writeBuzzerNote(result.query)
        else: result.writeNotFound()
            
    def writeHead(self, nStatus):  # response의 header
        self.send_response(nStatus)
        self.send_header('content-type', 'text/html') # 속성(attribute), 값 순으로 입력
        self.end_headers()

    def writeHtml(self, html):
        self.wfile.write(html.encode()) # html(유니코드) -> 바이트로 변경(encode() 함수 역할)

#=====================메인 Home HTML(Bootstrap 사용) ============================================================================
    def writeHome(self): # 홈용 HTML을 쓰기
        self.writeHead(200) # 200: 성공
        html = '''
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Hoseok's IoT Hub 페이지</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            <style>
                body {
                    background-image: url('https://behrtech.com/wp-content/uploads/2019/12/iStock-1013969318_optimized-2000x1200.jpg');
                    background-size: cover;
                    background-position: center;
                    background-repeat: no-repeat;
                    height: 100vh; /* 100% 화면 높이로 설정 */
                    margin: 0;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .container {
                    background-color: rgba(255, 255, 255, 0.8); /* 배경 색상과 투명도 조절 */
                    padding: 20px;
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container mt-5">
                <h1 class="text-center">Hoseok's IoT Hub 페이지</h1>
                <div class="row mt-4">
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title"><b>전압 측정</b></h5>
                                <button class="btn btn-primary btn-block" onclick="location.href='/meas_one_volt'">한 번 측정</button>
                                <form id="voltSamplingForm" onsubmit="submitVoltSamplingForm(); return false;"><br><br>
                                    <label for="voltCount">샘플링 개수:</label>
                                    <input type="number" class="form-control" id="voltCount" placeholder="개수 입력">
                                    <label for="voltDelay">샘플링 딜레이(sec):</label>
                                    <input type="number" class="form-control" id="voltDelay" placeholder="Delay 입력">
                                    <button type="submit" class="btn btn-primary btn-block mt-3">샘플링</button>
                                </form>
                            </div>
                        </div>
                        <div class="card mt-3">
                            <div class="card-body">
                                <h5 class="card-title"><b>조도 측정</b></h5>
                                <button class="btn btn-primary btn-block" onclick="location.href='/meas_one_light'">한 번 측정</button>
                                <form id="lightSamplingForm" onsubmit="submitLightSamplingForm(); return false;"><br><br>
                                    <label for="lightCount">샘플링 개수:</label>
                                    <input type="number" class="form-control" id="lightCount" placeholder="개수 입력">
                                    <label for="lightDelay">샘플링 딜레이(sec):</label>
                                    <input type="number" class="form-control" id="lightDelay" placeholder="Delay 입력">
                                    <button type="submit" class="btn btn-primary btn-block mt-3">샘플링</button>
                                </form>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title"><b>모터 제어</b></h5>
                                <button class="btn btn-info btn-block" onclick="location.href='/servo_move_0'">이동 0도</button>
                                <button class="btn btn-info btn-block" onclick="location.href='/servo_move_90'">이동 90도</button>
                                <button class="btn btn-info btn-block" onclick="location.href='/servo_move_180'">이동 180도</button>
                                <div class="mt-3"><br>
                                    <label for="motorSlider">자유 이동: <span id="motorValue">90</span>도</label>
                                    <input type="range" class="custom-range" id="motorSlider" min="0" max="180" step="1" value="90"
                                        oninput="updateMotorValue(this.value)">
                                    <button class="btn btn-warning btn-block" onclick="moveMotor()">이동</button>
                                </div>
                            </div>
                        </div>
                        <div class="card mt-3">
                            <div class="card-body">
                                <h5 class="card-title"><b>LED 제어</b></h5>
                                <label for="colorSelect">색상 선택:</label>
                                <select class="custom-select" id="colorSelect" onchange="selectColor()">
                                    <option value="red">Red</option>
                                    <option value="green">Green</option>
                                    <option value="blue">Blue</option>
                                    <option value="yellow">Yellow</option>
                                    <option value="cyan">Cyan</option>
                                    <option value="white">White</option>
                                </select>
                                <button class="btn btn-success btn-block mt-3" 
                                        onclick="location.href='/led?color='+document.getElementById('colorSelect').value">색상 출력</button>
                            </div>
                        </div>
                        <div class="card mt-3">
                            <div class="card-body">
                                <h5 class="card-title"><b>부저 제어</b></h5>
                                <form id="buzzerForm" onsubmit="submitBuzzerForm(); return false;">
                                    <label for="buzzerSelect">음 선택:</label>
                                    <select class="custom-select" id="buzzerSelect" onchange="selectBuzzer()">
                                        <option value="do">도 (C)</option>
                                        <option value="re">레 (D)</option>
                                        <option value="mi">미 (E)</option>
                                        <option value="fa">파 (F)</option>
                                        <option value="sol">솔 (G)</option>
                                        <option value="la">라 (A)</option>
                                        <option value="si">시 (B)</option>
                                    </select>
                                    <label for="buzzerDelay">연주 지연 시간(msec):</label>
                                    <input type="number" class="form-control" id="buzzerDelay" placeholder="Delay 입력">
                                    <button type="submit" class="btn btn-danger btn-block mt-3">연주</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
            <script>
                function moveMotor() {
                    var angle = document.getElementById('motorSlider').value;
                    location.href = '/servo_move?ang=' + angle;
                }
        
                function updateMotorValue(value) {
                    document.getElementById('motorValue').innerText = value;
                }
        
                function selectColor() {
                    var selectedColor = document.getElementById('colorSelect').value;
                }
        
                function selectBuzzer() {
                    var selectedNote = document.getElementById('buzzerSelect').value;
                }
        
                function submitVoltSamplingForm() {
                    var count = document.getElementById('voltCount').value;
                    var delay = document.getElementById('voltDelay').value;
                    location.href = '/sample_volt?count=' + count + '&delay=' + delay;
                }
        
                function submitLightSamplingForm() {
                    var count = document.getElementById('lightCount').value;
                    var delay = document.getElementById('lightDelay').value;
                    location.href = '/sample_light?count=' + count + '&delay=' + delay;
                }
        
                function submitBuzzerForm() {
                    var delay = document.getElementById('buzzerDelay').value;
                    var note = document.getElementById('buzzerSelect').value;
                    location.href = '/buzzer?note=' + note + '&delay=' + delay;
                }
            </script>
        </body>
        </html>
        '''

        self.writeHtml(html)

    def writeNotFound(self):
        self.writeHead(404) # 404: not found
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>페이지 없음</title>'
        html += '</head><body>'
        html += f'<div><h3>{self.path}에 대한 페이지는 존재하지 않습니다.</h3></div>'
        html += '</body></html>'
        self.writeHtml(html)
        
#=============전압 한 번 측정===========================================================================

    def writeMeasOneVolt(self):
        self.writeHead(200) # 200: 성공
        nTime = time.time()
        bResult = self.server.gateway.insertOneVoltTable() # gateway == PythonHub의 인스턴스
        if bResult: sResult = '성공'
        else: sResult = '실패'
        nMeasCount = self.server.gateway.countVoltTable()
        self.server.gateway.clearVoltTuple()
        self.server.gateway.loadVoltTupleFromTable()
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>전압 한 번 측정</title>'
        html += '</head><body>'
        html += f'<div><h5>측정 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>전압 측정이 {sResult}했습니다.</p>'
        html += f'<p>현재까지 {nMeasCount}번 측정했습니다.</div>'
        html += self.server.gateway.describeVoltTable()
        html += self.server.gateway.writeHtmlVoltTuple()
        html += '</body></html>'
        self.writeHtml(html)

#=============전압 샘플링===========================================================================

    def writeSampleVolt(self, qs):
        self.writeHead(200) # 200: 성공
        qdict = parse.parse_qs(qs)
        nCount = int(qdict['count'][0])
        delay = float(qdict['delay'][0])
        self.server.gateway.clearVoltTuple()
        nTime = time.time()
        self.server.gateway.sampleVoltTuple(nCount, delay)
        self.server.gateway.saveVoltTupleToTable()
        nMeasCount = self.server.gateway.countVoltTable()
        self.server.gateway.loadVoltTupleFromTable()
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>전압 여러 번 측정</title>'
        html += '</head><body>'
        html += f'<div><h5>측정 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>전압을 {nCount}번 샘플링했습니다.</p>'
        html += f'<p>현재까지 {nMeasCount}번 측정했습니다.</div>'
        html += self.server.gateway.describeVoltTable()
        html += self.server.gateway.writeHtmlVoltTuple()
        html += '</body></html>'
        self.writeHtml(html)

#=============조도 한 번 측정===========================================================================
    
    def writeMeasOneLight(self):
        self.writeHead(200) # 200: 성공
        nTime = time.time()
        bResult = self.server.gateway.insertOneLightTable() # gateway == PythonHub의 인스턴스
        if bResult: sResult = '성공'
        else: sResult = '실패'
        nMeasCount = self.server.gateway.countLightTable()
        self.server.gateway.clearLightTuple()
        self.server.gateway.loadLightTupleFromTable()
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>조도 한 번 측정</title>'
        html += '</head><body>'
        html += f'<div><h5>측정 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>조도 측정이 {sResult}번 했습니다.</p>'
        html += f'<p>현재까지 {nMeasCount}번 측정했습니다.</div>'
        html += self.server.gateway.describeLightTable()
        html += self.server.gateway.writeHtmlLightTuple()
        html += '</body></html>'
        self.writeHtml(html)
    
#=============조도 샘플링===========================================================================
    
    def writeSampleLight(self, qs):
        self.writeHead(200) # 200: 성공
        qdict = parse.parse_qs(qs)
        nCount = int(qdict['count'][0])
        delay = float(qdict['delay'][0])
        self.server.gateway.clearLightTuple()
        nTime = time.time()
        self.server.gateway.sampleLightTuple(nCount, delay)
        self.server.gateway.saveLightTupleToTable()
        nMeasCount = self.server.gateway.countLightTable()
        self.server.gateway.loadLightTupleFromTable()
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>조도 여러 번 측정</title>'
        html += '</head><body>'
        html += f'<div><h5>측정 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>조도를 {nCount}번 샘플링했습니다.</p>'
        html += f'<p>현재까지 {nMeasCount}번 측정했습니다.</div>'
        html += self.server.gateway.describeLightTable()
        html += self.server.gateway.writeHtmlLightTuple()
        html += '</body></html>'
        self.writeHtml(html)

#=============모터 이동 ===========================================================================

    def writeServoMove(self, ang):
        self.writeHead(200) # 200: 성공
        nTime = time.time()
        self.server.gateway.setServoMove(ang)
        html = '<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>모터 이동</title>'
        html += '</head><body>'
        html += f'<div><h5>이동 시작 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>모터를 {ang}도 위치로 이동했습니다.</p></div>'
        html += '</body></html>'
        self.writeHtml(html)

#=============모터 자유이동===========================================================================
    
    def writeServoMoveQs(self, qs):
        self.writeHead(200)  # 200: 성공
        qdict = parse.parse_qs(qs)
        nAng = int(qdict['ang'][0])
        nTime = time.time()
        self.server.gateway.setServoMove(nAng)
        html = f'<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>모터 이동</title>'
        html += '</head><body>'
        html += f'<div><h5>이동 시작 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>모터를 {nAng}도 위치로 이동했습니다.</p></div>'
        html += '</body></html>'
        self.writeHtml(html)

#=============led 색상 출력===========================================================================

    def writeLedColor(self, qs):
        self.writeHead(200)
        qdict = parse.parse_qs(qs)
        sColor = qdict.get('color', [''])[0]
        nTime = time.time()
        self.server.gateway.setLedColor(sColor)
        html = f'<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>불빛 확인</title>'
        html += '</head><body>'
        html += f'<div><h5>색상 선택 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>색상을 {sColor}로 선택하였습니다.</p></div>'
        html += '</body></html>'
        self.writeHtml(html)

#=============부저 연주================================================================================
    
    def writeBuzzerNote(self, qs):
        self.writeHead(200)
        qdict = parse.parse_qs(qs)
        sNote = qdict.get('note', [''])[0]
        nDelay = qdict.get('delay', [0])[0]
        nTime = time.time()
        self.server.gateway.setBuzzerNote(sNote, nDelay)
        html = f'<html><head>'
        html += '<meta http-equiv="content-type" content="text/html" charset="UTF-8">'
        html += '<title>부저 확인</title>'
        html += '</head><body>'
        html += f'<div><h5>부저 확인 시간: {time.ctime(nTime)}</h5></div>'
        html += f'<div><p>음계 {sNote}를 {nDelay}초 동안 소리가 들립니다.</p></div>'
        html += '</body></html>'
        self.writeHtml(html)

        


















        