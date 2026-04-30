import os
import shutil

# 1. 대상이 되는 28개 Run_ID 리스트 (스발바르 샘플)
target_run_ids = [
    'ERR5555225', 'ERR5554616', 'ERR8268598', 'ERR5554618', 'ERR5555200',
    'ERR8268645', 'ERR8268358', 'ERR5529627', 'ERR5529626', 'ERR5555350',
    'ERR5555214', 'ERR5847948', 'ERR8268656', 'ERR5529682', 'SRR18468278',
    'SRR22316775', 'SRR22316786', 'SRR22316787', 'SRR22316788', 'SRR22316791',
    'SRR22316794', 'ERR10878208', 'SRR23911158', 'ERR10878207', 'ERR10878209',
    'SRR23071390', 'SRR32260029', 'SRR32260032'
]

# 2. 파일을 저장할 새 폴더 생성
output_dir = "Svalbard_TPM_Results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"폴더 생성 완료: {output_dir}")

# 3. 현재 디렉토리의 파일 목록을 읽어 조건에 맞는 파일 복사
files_in_current_dir = os.listdir('.')
copied_count = 0

print("파일 복사 시작...")

for run_id in target_run_ids:
    # 각 Run_ID에 대해 '_tpm.png'로 끝나는 파일명 구성
    target_file_name = f"{run_id}_tpm.png"
    
    # 해당 파일이 현재 디렉토리에 존재하는지 확인
    if target_file_name in files_in_current_dir:
        shutil.copy(target_file_name, os.path.join(output_dir, target_file_name))
        print(f"복사 성공: {target_file_name}")
        copied_count += 1
    else:
        # 리스트에는 있지만 실제 파일이 없는 경우 출력 (확인용)
        # 예: 리스트의 SRR9952632 등은 위 28개 리스트에 포함되지 않음
        pass

print(f"\n--- 작업 완료 ---")
print(f"총 {copied_count}개의 파일이 '{output_dir}' 폴더로 복사되었습니다.")
