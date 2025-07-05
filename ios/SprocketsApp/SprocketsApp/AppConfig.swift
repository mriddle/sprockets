//
//  AppConfig.swift
//  SprocketsApp
//
//  Created by Matthew Riddle on 03/07/2025.
//

import Foundation

struct AppConfig {
    static var apiBaseURL: String {
        return value(for: "APIBaseURL")
    }

    private static func value<T>(for key: String) -> T {
        guard
            let url = Bundle.main.url(forResource: "AppConfig", withExtension: "plist"),
            let data = try? Data(contentsOf: url),
            let plist = try? PropertyListSerialization.propertyList(from: data, format: nil) as? [String: Any],
            let value = plist[key] as? T
        else {
            fatalError("\\(key) not set in AppConfig.plist")
        }
        return value
    }
}
