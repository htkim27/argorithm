def solution(numbers):
    # 숫자를 문자열로 변환
    numbers_str = [str(num) for num in numbers]
    # 문자열을 비교하여 큰 순서대로 정렬
    numbers_str.sort(key=lambda x: x*3, reverse=True)  # x*3은 문자열 비교를 위한 트릭 (1000 이하의 숫자를 고려)
    # 정렬된 문자열을 합쳐서 결과 생성
    answer = ''.join(numbers_str)
    # 모든 숫자가 0인 경우를 처리 ("0000" -> "0")
    return answer if answer[0] != '0' else '0'