import os
import shutil


stable_interface_list = ["luyaokun", "gaofangzhou", "laozhangren"]
stable_interface_pro_list = ["fuliming"]
beta_interface_list = ["zhangsan"]
temporary_interface_list = ["lisi"]
discarded_name_list = ["wangwu"]
backlist = ["zhaoliu"]
summary_name_list = tuple(stable_interface_list + stable_interface_pro_list + beta_interface_list + temporary_interface_list)


def distribute_interface():
    return_data = dict()
    return_data["status_code"] = 0
    try:
        # 分发stable渠道
        for name in stable_interface_list:
            target_path = f"./distribute/{name}.json"
            shutil.copy2("./stableinterface.json", target_path)
    except:
        pass
    finally:
        pass


if __name__ == "__main__":
    distribute_interface()