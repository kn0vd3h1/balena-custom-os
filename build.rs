use std::process::Command;

fn main() {
    Command::new("bash")
        .arg("setup.sh")
        .status()
        .unwrap();
}
