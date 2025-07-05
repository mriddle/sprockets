import SwiftUI

struct ContentView: View {
    @State private var message: String = "Loading..."
    @State private var error: String?

    var body: some View {
        VStack(spacing: 20) {
            if let error = error {
                Text("Error: \(error)")
                    .foregroundColor(.red)
            } else {
                Text(message)
                    .font(.title)
            }
            Button("Reload") {
                fetchHello()
            }
        }
        .padding()
        .onAppear(perform: fetchHello)
    }

    func fetchHello() {
        guard let url = URL(string: "\(AppConfig.apiBaseURL)/hello-ios") else {
            self.error = "Invalid URL"
            return
        }
        error = nil
        message = "Loading..."
        let task = URLSession.shared.dataTask(with: url) { data, response, err in
            if let err = err {
                DispatchQueue.main.async {
                    self.error = err.localizedDescription
                }
                return
            }
            guard let data = data else {
                DispatchQueue.main.async {
                    self.error = "No data"
                }
                return
            }
            do {
                if let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
                   let msg = json["message"] as? String {
                    DispatchQueue.main.async {
                        self.message = msg
                    }
                } else {
                    DispatchQueue.main.async {
                        self.error = "Invalid response"
                    }
                }
            } catch {
                DispatchQueue.main.async {
                    self.error = error.localizedDescription
                }
            }
        }
        task.resume()
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
